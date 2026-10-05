"""High-confidence source-secret and frontend-boundary checks; not a penetration test."""
from __future__ import annotations

import argparse
from pathlib import Path
import re
import subprocess

TOKEN_PATTERNS = (
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    re.compile(r"\bgh[pousr]_[A-Za-z0-9]{30,}\b"),
    re.compile(r"\bAKIA[A-Z0-9]{16}\b"),
    re.compile(r"\bsk-(?:proj-|ant-)[A-Za-z0-9_-]{25,}\b"),
    re.compile(r"postgres(?:ql)?(?:\+[a-z]+)?://[^:\s]+:([^@\s]+)@"),
)


def inspect_source(path: str, text: str) -> list[str]:
    issues = []
    if Path(path).name == '.env' or path.startswith(('secrets/', 'backups/', 'learner-exports/')):
        issues.append('forbidden private-data path')
    if any(pattern.search(text) for pattern in TOKEN_PATTERNS):
        issues.append('possible credential or private key (value withheld)')
    return issues


def inspect_bundle(directory: Path) -> list[str]:
    if not directory.is_dir():
        return ['frontend build missing']
    issues = []
    for path in directory.rglob('*'):
        if path.is_file():
            text = path.read_text(encoding='utf-8', errors='ignore')
            if any(marker in text for marker in ('solution_spec', 'PRIVATE_TEST_SENTINEL', 'question-banks/practice.json', 'lattice-academy:v1')):
                issues.append(f'{path.name}: private authoring or legacy payload marker in default frontend')
    return issues


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('--bundle', type=Path)
    args = parser.parse_args()
    files = subprocess.check_output(['git', 'ls-files', '--cached', '--others', '--exclude-standard', '-z'], cwd=args.root).decode().split('\0')
    failures = []
    scanned = 0
    for relative in sorted(set(files) - {''}):
        path = args.root / relative
        if not path.is_file():
            continue
        text = path.read_text(encoding='utf-8', errors='ignore')
        for issue in inspect_source(relative, text):
            failures.append(f'{relative}: {issue}')
        scanned += 1
    if args.bundle:
        failures.extend(inspect_bundle(args.bundle))
    print(f'Security boundary scan: {scanned} source files; {len(failures)} finding(s).')
    for failure in failures:
        print(failure)
    return 1 if failures else 0


if __name__ == '__main__':
    raise SystemExit(main())
