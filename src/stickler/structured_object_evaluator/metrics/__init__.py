"""Metrics calculation for structured object evaluation.

Computes confusion-matrix counts and derived metrics (precision, recall, F1):

- ``confusion_matrix_calculator.py`` -- ConfusionMatrixCalculator
- ``confusion_matrix_builder.py`` -- ConfusionMatrixBuilder
- ``aggregate.py`` -- AggregateMetricsCalculator
- ``derived.py`` -- DerivedMetricsCalculator (precision / recall / F1)
- ``confidence.py`` -- ConfidenceCalculator (AUROC)
- ``helpers.py`` -- MetricsHelper

Depends on: ``core``, ``comparators``, ``model_def``, ``comparison``
"""

from .aggregate import AggregateMetricsCalculator
from .confidence import ConfidenceCalculator
from .confusion_matrix_builder import ConfusionMatrixBuilder
from .confusion_matrix_calculator import ConfusionMatrixCalculator
from .derived import DerivedMetricsCalculator
from .helpers import MetricsHelper

__all__ = [
    "AggregateMetricsCalculator",
    "ConfusionMatrixCalculator",
    "ConfusionMatrixBuilder",
    "DerivedMetricsCalculator",
    "ConfidenceCalculator",
    "MetricsHelper",
]
