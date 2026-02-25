"""Backward-compatibility shim. Import from stickler.structured_object_evaluator.evaluation.single instead."""

from ..evaluation.single import compare_json

__all__ = ["compare_json"]
