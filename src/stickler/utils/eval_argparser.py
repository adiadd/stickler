"""Backward-compatibility shim. Import from stickler.utils.argparser instead."""

import warnings as _warnings
_warnings.warn(
    "Import from stickler.utils.argparser instead. This shim will be removed in v0.3.0.",
    DeprecationWarning,
    stacklevel=2,
)

from stickler.utils.argparser import get_args

__all__ = ["get_args"]
