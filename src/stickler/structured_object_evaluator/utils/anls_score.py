"""Backward-compatibility shim. Import from stickler.structured_object_evaluator.evaluation.single instead."""

from ..evaluation.single import anls_score, compare_json, compare_structured_models

__all__ = ["anls_score", "compare_json", "compare_structured_models"]
