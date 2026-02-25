"""Backward-compatibility shim. Import from stickler.structured_object_evaluator.core.field instead."""

from stickler.structured_object_evaluator.core.field import (
    ComparableFieldConfig,
    ComparisonInfo,
    add_comparison_schema,
)

__all__ = ["ComparisonInfo", "ComparableFieldConfig", "add_comparison_schema"]
