"""Backward-compatibility shim. Import from stickler.reporting.markdown instead."""

import warnings as _warnings
_warnings.warn(
    "Import from stickler.reporting.markdown instead. This shim will be removed in v0.3.0.",
    DeprecationWarning,
    stacklevel=2,
)

from stickler.reporting.markdown import MarkdownUtil

__all__ = ["MarkdownUtil"]
