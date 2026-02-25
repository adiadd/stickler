"""Backward-compatibility shim. Import from stickler.structured_object_evaluator.evaluation.bulk instead."""

from .evaluation.bulk import BulkStructuredModelEvaluator, aggregate_from_comparisons

__all__ = ["BulkStructuredModelEvaluator", "aggregate_from_comparisons"]
