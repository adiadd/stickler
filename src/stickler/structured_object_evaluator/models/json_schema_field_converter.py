"""Backward-compatibility shim. Import from stickler.structured_object_evaluator.model_def.json_schema_converter instead."""

from ..model_def.json_schema_converter import (
    JsonSchemaFieldConverter,
)

__all__ = ["JsonSchemaFieldConverter"]
