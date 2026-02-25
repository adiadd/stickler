"""Backward-compatibility shim. Import from stickler.structured_object_evaluator.model_def.json_schema_validator instead."""

from ..model_def.json_schema_validator import validate_json_schema, validate_instance_against_schema

__all__ = ["validate_json_schema", "validate_instance_against_schema"]
