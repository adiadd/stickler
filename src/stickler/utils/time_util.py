"""Backward-compatibility shim. Import from stickler.utils.time instead."""

import warnings as _warnings

_warnings.warn(
    "Import from stickler.utils.time instead. This shim will be removed in v0.3.0.",
    DeprecationWarning,
    stacklevel=2,
)

from stickler.utils.time import sleep

__all__ = ["sleep"]
