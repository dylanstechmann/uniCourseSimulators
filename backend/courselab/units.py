"""Small, explicit unit-conversion grammar for deterministic practice grading.

This is deliberately not a general unit package. Unknown or affine units fail
closed so the grader never guesses about a scientific quantity. A few
contextual labels are accepted only as exact, non-composable symbols.
"""

import re
from dataclasses import dataclass
from decimal import Decimal
from fractions import Fraction


class UnitParseError(ValueError):
    """A unit is malformed, unknown, or outside this grader's supported subset."""


# Base dimension order: length, mass, time, current, temperature, amount,
# luminous intensity. Scales are relative to SI base units.
DIMENSION_COUNT = 7
ZERO_DIMENSIONS = (0,) * DIMENSION_COUNT


@dataclass(frozen=True)
class Unit:
    scale: Fraction
    dimensions: tuple[int, ...]
    context: str | None = None


def _dims(**powers: int) -> tuple[int, ...]:
    keys = ("length", "mass", "time", "current", "temperature", "amount", "luminous_intensity")
    return tuple(powers.get(key, 0) for key in keys)


def _atom(scale: str, **powers: int) -> Unit:
    return Unit(Fraction(Decimal(scale)), _dims(**powers))


_ATOMS = {
    "1": _atom("1"),
    "fraction": _atom("1"),
    "%": _atom("0.01"),
    "rad": _atom("1"),
    "m": _atom("1", length=1),
    "km": _atom("1000", length=1),
    "cm": _atom("0.01", length=1),
    "mm": _atom("0.001", length=1),
    "μm": _atom("0.000001", length=1),
    "nm": _atom("1e-9", length=1),
    "kg": _atom("1", mass=1),
    "g": _atom("0.001", mass=1),
    "mg": _atom("1e-6", mass=1),
    "μg": _atom("1e-9", mass=1),
    "s": _atom("1", time=1),
    "ms": _atom("0.001", time=1),
    "μs": _atom("1e-6", time=1),
    "min": _atom("60", time=1),
    "h": _atom("3600", time=1),
    "A": _atom("1", current=1),
    "mA": _atom("0.001", current=1),
    "μA": _atom("1e-6", current=1),
    "nA": _atom("1e-9", current=1),
    "pA": _atom("1e-12", current=1),
    "K": _atom("1", temperature=1),
    "mol": _atom("1", amount=1),
    "molATP": Unit(Fraction(1), _dims(amount=1), context="ATP amount"),
    "mmol": _atom("0.001", amount=1),
    "μmol": _atom("1e-6", amount=1),
    "nmol": _atom("1e-9", amount=1),
    # Liter is exactly 1 dm^3. M and its listed prefixes mean mol/L.
    "L": _atom("0.001", length=3),
    "mL": _atom("1e-6", length=3),
    "μL": _atom("1e-9", length=3),
    "M": _atom("1000", amount=1, length=-3),
    "mM": _atom("1", amount=1, length=-3),
    "μM": _atom("0.001", amount=1, length=-3),
    "nM": _atom("1e-6", amount=1, length=-3),
    "Hz": _atom("1", time=-1),
    "N": _atom("1", length=1, mass=1, time=-2),
    "J": _atom("1", length=2, mass=1, time=-2),
    "kJ": _atom("1000", length=2, mass=1, time=-2),
    "μJ": _atom("1e-6", length=2, mass=1, time=-2),
    "W": _atom("1", length=2, mass=1, time=-3),
    "Pa": _atom("1", length=-1, mass=1, time=-2),
    "MPa": _atom("1e6", length=-1, mass=1, time=-2),
    "C": _atom("1", time=1, current=1),
    "V": _atom("1", length=2, mass=1, time=-3, current=-1),
    "mV": _atom("0.001", length=2, mass=1, time=-3, current=-1),
    "MV": _atom("1e6", length=2, mass=1, time=-3, current=-1),
    "Ω": _atom("1", length=2, mass=1, time=-3, current=-2),
    "pH": Unit(Fraction(1), ZERO_DIMENSIONS, context="pH"),
    "units": Unit(Fraction(1), ZERO_DIMENSIONS, context="assay-unit"),
}
# ASCII-u spellings are accepted as common keyboard alternatives to μ.
for _alias, _canonical in {
    "um": "μm", "ug": "μg", "us": "μs", "uA": "μA", "umol": "μmol",
    "uL": "μL", "uM": "μM", "uJ": "μJ",
}.items():
    _ATOMS[_alias] = _ATOMS[_canonical]

_TOKEN = re.compile(r"[A-Za-zμ]+|Ω|%|1|[()+*/·^+-]|\d+")
_SUPERSCRIPT_DIGITS = str.maketrans("⁰¹²³⁴⁵⁶⁷⁸⁹", "0123456789")
_SUPERSCRIPT_RUN = re.compile(r"([⁺⁻]?)([⁰¹²³⁴⁵⁶⁷⁸⁹]+)")


def _normalized(value: str) -> str:
    value = value.replace("µ", "μ").replace("⋅", "·")
    value = re.sub(r"\bmol\s+ATP\b", "molATP", value)
    return _SUPERSCRIPT_RUN.sub(
        lambda match: "^" + ("-" if match[1] == "⁻" else "+" if match[1] == "⁺" else "")
        + match[2].translate(_SUPERSCRIPT_DIGITS),
        value,
    )


class _Parser:
    def __init__(self, value: str):
        normalized = _normalized(value).replace(" ", "")
        if len(normalized) > 80:
            raise UnitParseError("Unit expression is too long")
        self.tokens = _TOKEN.findall(normalized)
        if "".join(self.tokens) != normalized or len(self.tokens) > 48:
            raise UnitParseError("Malformed unit expression")
        self.position = 0

    def peek(self) -> str | None:
        return self.tokens[self.position] if self.position < len(self.tokens) else None

    def take(self) -> str:
        token = self.peek()
        if token is None:
            raise UnitParseError("Incomplete unit expression")
        self.position += 1
        return token

    def expression(self) -> Unit:
        result = self.factor()
        while self.peek() in {"*", "·", "/"}:
            operator = self.take()
            other = self.factor()
            if result.context is not None or other.context is not None:
                raise UnitParseError("Contextual units cannot be composed or converted")
            if operator == "/":
                result = Unit(result.scale / other.scale, tuple(a - b for a, b in zip(result.dimensions, other.dimensions)))
            else:
                result = Unit(result.scale * other.scale, tuple(a + b for a, b in zip(result.dimensions, other.dimensions)))
            if any(abs(power) > 24 for power in result.dimensions):
                raise UnitParseError("Unit dimensions exceed the supported range")
        return result

    def factor(self) -> Unit:
        if self.peek() == "(":
            self.take()
            result = self.expression()
            if self.take() != ")":
                raise UnitParseError("Unbalanced unit parentheses")
        else:
            symbol = self.take()
            if symbol not in _ATOMS:
                raise UnitParseError(f"Unsupported unit symbol: {symbol}")
            result = _ATOMS[symbol]
        if self.peek() == "^":
            self.take()
            if result.context is not None:
                raise UnitParseError("Contextual units cannot have exponents")
            sign = 1
            if self.peek() in {"+", "-"}:
                sign = -1 if self.take() == "-" else 1
            token = self.take()
            if not token.isdigit() or len(token) > 2:
                raise UnitParseError("Invalid unit exponent")
            exponent = sign * int(token)
            if abs(exponent) > 12:
                raise UnitParseError("Unit exponent exceeds the supported range")
            result = Unit(result.scale**exponent, tuple(power * exponent for power in result.dimensions))
            if any(abs(power) > 24 for power in result.dimensions):
                raise UnitParseError("Unit dimensions exceed the supported range")
        return result


def parse_unit(value: str | None) -> Unit:
    """Parse a supported multiplicative unit expression; empty means dimensionless."""
    if value is None or not value.strip():
        return Unit(Fraction(1), ZERO_DIMENSIONS)
    parser = _Parser(value)
    result = parser.expression()
    if parser.peek() is not None:
        raise UnitParseError("Unexpected token in unit expression")
    return result


def dimensions_from_spec(value: object) -> tuple[int, ...]:
    if not isinstance(value, dict) or not value:
        raise UnitParseError("Authored dimensions must be a non-empty dimension mapping")
    keys = ("length", "mass", "time", "current", "temperature", "amount", "luminous_intensity")
    if set(value) - set(keys):
        raise UnitParseError("Authored dimensions contain an unsupported base dimension")
    powers: list[int] = []
    for key in keys:
        power = value.get(key, 0)
        if type(power) is not int or abs(power) > 12:
            raise UnitParseError("Authored dimensions must use integer powers from -12 through 12")
        powers.append(power)
    return tuple(powers)
