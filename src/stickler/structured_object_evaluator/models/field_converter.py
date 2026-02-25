"""Backward-compatibility shim. Import from stickler.structured_object_evaluator.model_def.field_converter instead."""

from stickler.structured_object_evaluator.model_def.field_converter import (
    FieldConverter,
    _global_converter,
    convert_field_config,
    convert_fields_config,
    get_global_converter,
    validate_field_config,
    validate_fields_config,
)

__all__ = [
    "FieldConverter",
    "_global_converter",
    "get_global_converter",
    "convert_field_config",
    "convert_fields_config",
    "validate_field_config",
    "validate_fields_config",
]
