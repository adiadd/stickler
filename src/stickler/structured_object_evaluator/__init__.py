"""Structured object evaluator package.

This package provides tools for evaluating structured objects using configurable
comparison metrics and displaying the results in a user-friendly format.
"""

from .evaluation.bulk import aggregate_from_comparisons
from .model_def.comparable_field import ComparableField
from .core.non_match import NonMatchField, NonMatchType
from .model_def.structured_model import StructuredModel
from .evaluation.single import anls_score, compare_json, compare_structured_models
from .evaluation.key_scores import ScoreNode, construct_nested_dict, merge_and_calculate_mean
from stickler.reporting.text import print_confusion_matrix, print_confusion_matrix_html

__all__ = [
    "StructuredModel",
    "ComparableField",
    "NonMatchField",
    "NonMatchType",
    "compare_structured_models",
    "anls_score",
    "compare_json",
    "aggregate_from_comparisons",
    "ScoreNode",
    "construct_nested_dict",
    "merge_and_calculate_mean",
    "print_confusion_matrix",
    "print_confusion_matrix_html",
]
