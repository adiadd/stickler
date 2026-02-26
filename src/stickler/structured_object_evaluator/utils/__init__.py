"""Utility functions for structured object evaluation."""

import warnings as _warnings

_warnings.warn(
    "Import from stickler.structured_object_evaluator.evaluation instead. "
    "This shim will be removed in v0.3.0.",
    DeprecationWarning,
    stacklevel=2,
)

from ..evaluation.key_scores import (
    ScoreNode,
    construct_nested_dict,
    merge_and_calculate_mean,
)
from ..evaluation.single import anls_score, compare_json, compare_structured_models

__all__ = [
    "ScoreNode",
    "construct_nested_dict",
    "merge_and_calculate_mean",
    "compare_structured_models",
    "anls_score",
    "compare_json",
]
