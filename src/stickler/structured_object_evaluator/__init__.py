"""Structured object evaluator package.

This package provides tools for evaluating structured objects using configurable
comparison metrics and displaying the results in a user-friendly format.
"""

from stickler.reporting.text import print_confusion_matrix, print_confusion_matrix_html

from .core.non_match import NonMatchField, NonMatchType
from .evaluation.bulk import aggregate_from_comparisons
from .evaluation.key_scores import (
    ScoreNode,
    construct_nested_dict,
    merge_and_calculate_mean,
)
from .evaluation.single import anls_score, compare_json, compare_structured_models
from .model_def.comparable_field import ComparableField
from .model_def.structured_model import StructuredModel

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
