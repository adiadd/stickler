"""Backward-compatibility shim. Import from stickler.reporting.text instead."""

import warnings as _warnings

_warnings.warn(
    "Import from stickler.reporting.text instead. This shim will be removed in v0.3.0.",
    DeprecationWarning,
    stacklevel=2,
)

from stickler.reporting.text import (
    Colors,
    print_confusion_matrix,
    print_confusion_matrix_html,
    print_evaluation_results,
    print_non_matches,
)

__all__ = [
    "Colors",
    "print_confusion_matrix",
    "print_confusion_matrix_html",
    "print_evaluation_results",
    "print_non_matches",
]
