"""Backward-compatibility shim. Import from stickler.structured_object_evaluator.model_def.comparable_field instead."""

from stickler.structured_object_evaluator.model_def.comparable_field import (
    ComparableField,
    _reconstruct_comparator_from_type,
    add_comparison_schema,
)

__all__ = ["ComparableField", "_reconstruct_comparator_from_type", "add_comparison_schema"]
