"""Backward-compatibility shim. Import from stickler.structured_object_evaluator.evaluation.key_scores instead."""

from ..evaluation.key_scores import ScoreNode, construct_nested_dict, merge_and_calculate_mean

__all__ = ["ScoreNode", "construct_nested_dict", "merge_and_calculate_mean"]
