"""High-level evaluation orchestration for structured object evaluation.

Provides the public-facing evaluation functions and bulk evaluator:

- ``single.py`` -- compare_structured_models, anls_score, compare_json
- ``bulk.py`` -- BulkStructuredModelEvaluator, aggregate_from_comparisons
- ``format_helper.py`` -- EvaluatorFormatHelper
- ``non_match_collector.py`` -- NonMatchCollector
- ``non_matches_helper.py`` -- NonMatchesHelper
- ``field_comparison_collector.py`` -- FieldComparisonCollector
- ``field_comparison_helper.py`` -- FieldComparisonHelper
- ``key_scores.py`` -- ScoreNode and score utilities
- ``anls/`` -- ANLS* tree-based evaluation sub-package

Depends on: ``core``, ``comparators``, ``model_def``, ``comparison``, ``metrics``
"""

from .bulk import BulkStructuredModelEvaluator, aggregate_from_comparisons
from .key_scores import ScoreNode, construct_nested_dict, merge_and_calculate_mean
from .single import anls_score, compare_json, compare_structured_models

__all__ = [
    "anls_score",
    "compare_json",
    "compare_structured_models",
    "BulkStructuredModelEvaluator",
    "aggregate_from_comparisons",
    "ScoreNode",
    "construct_nested_dict",
    "merge_and_calculate_mean",
]
