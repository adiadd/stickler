"""Backward-compatibility shim. Import from stickler.structured_object_evaluator.comparison.helpers_base instead."""

from ..comparison.helpers_base import (
    ComparisonHelperBase,
    DEFAULT_MATCH_THRESHOLD,
)

__all__ = ["ComparisonHelperBase", "DEFAULT_MATCH_THRESHOLD"]
