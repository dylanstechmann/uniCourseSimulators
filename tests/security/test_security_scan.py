from tools.check_security import inspect_bundle, inspect_source


def test_rejects_private_paths_and_credentials():
    assert inspect_source('.env', 'not-a-real-secret')
    assert inspect_source('backups/user.dump', 'synthetic')
    assert inspect_source('config.py', 'postgresql://' + 'synthetic:fixture@db/database')
    assert inspect_source('config.py', 'gh' + 'p_' + 'a' * 36)
    assert not inspect_source('.env.example', 'DB_PASSWORD_FILE=\nCOURSELAB_DOMAIN=')


def test_build_must_exclude_solution_data(tmp_path):
    assert inspect_bundle(tmp_path / 'missing')
    (tmp_path / 'app.js').write_text('public frontend only')
    assert not inspect_bundle(tmp_path)
    (tmp_path / 'leaked.js').write_text('solution_' + 'spec')
    assert inspect_bundle(tmp_path)
