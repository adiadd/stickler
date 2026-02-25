"""Backward-compatibility shim. Import from stickler.structured_object_evaluator.evaluation.key_scores instead."""

import warnings as _warnings
_warnings.warn(
    "Import from stickler.structured_object_evaluator.evaluation.key_scores instead. This shim will be removed in v0.3.0.",
    DeprecationWarning,
    stacklevel=2,
)

from ..evaluation.key_scores import (
    ScoreNode,
    construct_nested_dict,
    merge_and_calculate_mean,
)

__all__ = ["ScoreNode", "construct_nested_dict", "merge_and_calculate_mean"]
