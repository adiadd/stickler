"""Backward-compatibility shim — use ``stickler.reporting`` instead."""

import warnings as _warnings

_warnings.warn(
    "Import from stickler.reporting instead. This shim will be removed in v0.3.0.",
    DeprecationWarning,
    stacklevel=2,
)
