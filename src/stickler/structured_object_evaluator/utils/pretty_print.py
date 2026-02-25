"""Backward-compatibility shim. Import from stickler.reporting.text instead."""

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
