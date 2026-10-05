"""Bounded rational-expression parsing and equivalence checks for practice items.

Learner text is parsed with Python's AST only as a syntax tree. No Python source
is evaluated, and only arithmetic nodes from the small allowlist below become
SymPy expressions.
"""

from __future__ import annotations

import ast
import math
import re
from dataclasses import dataclass

import sympy as sp


class SymbolicExpressionError(ValueError):
    """The expression or authored symbolic specification is outside policy."""


MAX_EXPRESSION_LENGTH = 256
MAX_AST_NODES = 64
MAX_AST_DEPTH = 14
MAX_VARIABLES = 8
MAX_TERMS = 128
MAX_DEGREE = 64
MAX_ABS_EXPONENT = 8
MAX_OPERATIONS = 512

_VARIABLE = re.compile(r"^[A-Za-z][A-Za-z0-9_]{0,31}$")
_INTEGER = re.compile(r"^\d{1,18}$")
_DECIMAL = re.compile(r"^(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?$")
_DECIMAL_EXPONENT = re.compile(r"[eE]([+-]?\d+)$")
_ASSUMPTIONS = {"real", "positive", "nonnegative", "nonzero", "integer"}


@dataclass(frozen=True)
class _RationalBudget:
    numerator_terms: int
    denominator_terms: int
    numerator_degree: int
    denominator_degree: int


def _bounded(value: _RationalBudget) -> _RationalBudget:
    if (
        value.numerator_terms > MAX_TERMS
        or value.denominator_terms > MAX_TERMS
        or value.numerator_degree > MAX_DEGREE
        or value.denominator_degree > MAX_DEGREE
    ):
        raise SymbolicExpressionError("Expression exceeds the symbolic complexity limits")
    return value


def _depth(node: ast.AST) -> int:
    children = list(ast.iter_child_nodes(node))
    return 1 + max((_depth(child) for child in children), default=0)


def _power_terms(terms: int, exponent: int) -> int:
    if exponent == 0:
        return 1
    return math.comb(terms + exponent - 1, exponent)


def _literal_exponent(node: ast.AST, source: str) -> int:
    sign = 1
    value = node
    if isinstance(value, ast.UnaryOp) and isinstance(value.op, (ast.UAdd, ast.USub)):
        sign = -1 if isinstance(value.op, ast.USub) else 1
        value = value.operand
    if not isinstance(value, ast.Constant) or type(value.value) is not int:
        raise SymbolicExpressionError("Exponent must be a small integer literal")
    token = ast.get_source_segment(source, value)
    if token is None or not _INTEGER.fullmatch(token):
        raise SymbolicExpressionError("Exponent must be a small integer literal")
    exponent = sign * int(token)
    if abs(exponent) > MAX_ABS_EXPONENT:
        raise SymbolicExpressionError("Exponent exceeds the symbolic complexity limits")
    return exponent


def _validate_spec(variables: object, assumptions: object) -> dict[str, sp.Symbol]:
    if (
        not isinstance(variables, list)
        or not 1 <= len(variables) <= MAX_VARIABLES
        or any(not isinstance(name, str) or not _VARIABLE.fullmatch(name) for name in variables)
        or len(set(variables)) != len(variables)
    ):
        raise SymbolicExpressionError("Authored variables must be 1–8 unique simple names")
    if not isinstance(assumptions, dict) or len(assumptions) > len(variables):
        raise SymbolicExpressionError("Authored assumptions must map declared variables to supported flags")
    if set(assumptions) - set(variables):
        raise SymbolicExpressionError("Assumptions may only reference declared variables")

    symbols: dict[str, sp.Symbol] = {}
    try:
        for name in variables:
            flags = assumptions.get(name, {})
            if (
                not isinstance(flags, dict)
                or len(flags) > len(_ASSUMPTIONS)
                or set(flags) - _ASSUMPTIONS
                or any(type(value) is not bool for value in flags.values())
            ):
                raise SymbolicExpressionError("An authored variable assumption is invalid")
            symbols[name] = sp.Symbol(name, **flags)
    except (TypeError, ValueError) as exc:
        if isinstance(exc, SymbolicExpressionError):
            raise
        raise SymbolicExpressionError("Authored variable assumptions are inconsistent") from exc
    return symbols


def parse_expression(source: str, symbols: dict[str, sp.Symbol]) -> sp.Expr:
    """Parse a bounded arithmetic expression without evaluating learner code."""
    if not isinstance(source, str) or not source.strip() or len(source) > MAX_EXPRESSION_LENGTH:
        raise SymbolicExpressionError("Expression must contain 1–256 characters")
    if sum(character.isdigit() for character in source) > 96:
        raise SymbolicExpressionError("Expression contains too many numeric digits")
    # Caret is conventional exponent notation for learners but Python assigns
    # it bitwise-XOR precedence. Normalize it before syntax parsing so sums and
    # products retain ordinary mathematical precedence.
    source = source.replace("^", "**")
    try:
        tree = ast.parse(source, mode="eval")
    except (SyntaxError, ValueError, RecursionError) as exc:
        raise SymbolicExpressionError("Expression syntax is not supported") from exc
    nodes = list(ast.walk(tree))
    if len(nodes) > MAX_AST_NODES or _depth(tree) > MAX_AST_DEPTH:
        raise SymbolicExpressionError("Expression exceeds the symbolic complexity limits")

    def visit(node: ast.AST) -> tuple[sp.Expr, _RationalBudget]:
        if isinstance(node, ast.Expression):
            return visit(node.body)
        if isinstance(node, ast.Constant):
            if type(node.value) not in (int, float):
                raise SymbolicExpressionError("Only finite decimal or integer constants are supported")
            token = ast.get_source_segment(source, node)
            if token is None:
                raise SymbolicExpressionError("Numeric literal could not be read")
            if type(node.value) is int and _INTEGER.fullmatch(token):
                number = sp.Integer(token)
            elif type(node.value) is float and _DECIMAL.fullmatch(token):
                exponent = _DECIMAL_EXPONENT.search(token)
                if exponent and abs(int(exponent.group(1))) > 12:
                    raise SymbolicExpressionError("Decimal exponent exceeds the symbolic complexity limits")
                number = sp.Rational(token)
            else:
                raise SymbolicExpressionError("Only ordinary base-10 numeric literals are supported")
            budget = _RationalBudget(1, 1, 0, 0)
        elif isinstance(node, ast.Name):
            if node.id not in symbols:
                raise SymbolicExpressionError("Expression uses an undeclared variable")
            number = symbols[node.id]
            budget = _RationalBudget(1, 1, 1, 0)
        elif isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.UAdd, ast.USub)):
            number, budget = visit(node.operand)
            if isinstance(node.op, ast.USub):
                number = -number
        elif isinstance(node, ast.BinOp) and isinstance(node.op, (ast.Add, ast.Sub, ast.Mult, ast.Div, ast.Pow, ast.BitXor)):
            left, a = visit(node.left)
            if isinstance(node.op, (ast.Pow, ast.BitXor)):
                exponent = _literal_exponent(node.right, source)
                magnitude = abs(exponent)
                if exponent >= 0:
                    budget = _bounded(_RationalBudget(
                        _power_terms(a.numerator_terms, magnitude),
                        _power_terms(a.denominator_terms, magnitude),
                        a.numerator_degree * magnitude,
                        a.denominator_degree * magnitude,
                    ))
                    number = left**exponent
                else:
                    budget = _bounded(_RationalBudget(
                        _power_terms(a.denominator_terms, magnitude),
                        _power_terms(a.numerator_terms, magnitude),
                        a.denominator_degree * magnitude,
                        a.numerator_degree * magnitude,
                    ))
                    number = left**exponent
            else:
                right, b = visit(node.right)
                if isinstance(node.op, (ast.Add, ast.Sub)):
                    budget = _bounded(_RationalBudget(
                        a.numerator_terms * b.denominator_terms
                        + b.numerator_terms * a.denominator_terms,
                        a.denominator_terms * b.denominator_terms,
                        max(
                            a.numerator_degree + b.denominator_degree,
                            b.numerator_degree + a.denominator_degree,
                        ),
                        a.denominator_degree + b.denominator_degree,
                    ))
                    number = left + right if isinstance(node.op, ast.Add) else left - right
                elif isinstance(node.op, ast.Mult):
                    budget = _bounded(_RationalBudget(
                        a.numerator_terms * b.numerator_terms,
                        a.denominator_terms * b.denominator_terms,
                        a.numerator_degree + b.numerator_degree,
                        a.denominator_degree + b.denominator_degree,
                    ))
                    number = left * right
                else:
                    budget = _bounded(_RationalBudget(
                        a.numerator_terms * b.denominator_terms,
                        a.denominator_terms * b.numerator_terms,
                        a.numerator_degree + b.denominator_degree,
                        a.denominator_degree + b.numerator_degree,
                    ))
                    number = left / right
        else:
            raise SymbolicExpressionError("Only arithmetic, parentheses, and declared variables are supported")

        if number.has(sp.zoo, sp.oo, -sp.oo, sp.nan, sp.I):
            raise SymbolicExpressionError("Expression is undefined or outside the real rational domain")
        if sp.count_ops(number) > MAX_OPERATIONS:
            raise SymbolicExpressionError("Expression exceeds the symbolic complexity limits")
        return number, budget

    result, _ = visit(tree)
    return result


def prepare_answer(
    expected: object, variables: object, assumptions: object
) -> tuple[dict[str, sp.Symbol], sp.Expr]:
    """Validate and parse the authored answer separately from learner input."""
    if not isinstance(expected, str):
        raise SymbolicExpressionError("Authored expression must be text")
    symbols = _validate_spec(variables, assumptions)
    answer = parse_expression(expected, symbols)
    return symbols, answer


def matches_expected(response: str, symbols: dict[str, sp.Symbol], expected: sp.Expr) -> bool:
    """Parse one learner expression and compare it by bounded rational cancellation."""
    learner = parse_expression(response, symbols)
    return sp.cancel(learner - expected) == 0


def equivalent(response: str, expected: str, variables: object, assumptions: object) -> bool:
    """Return rational-function equivalence using targeted cancellation only."""
    symbols, answer = prepare_answer(expected, variables, assumptions)
    return matches_expected(response, symbols, answer)
