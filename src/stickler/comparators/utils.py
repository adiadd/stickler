"""Backward-compatibility shim. Import from stickler.comparators._embedding_utils instead."""

import warnings as _warnings

_warnings.warn(
    "Import from stickler.comparators._embedding_utils instead. This shim will be removed in v0.3.0.",
    DeprecationWarning,
    stacklevel=2,
)

from ._embedding_utils import generate_bedrock_embedding

__all__ = ["generate_bedrock_embedding"]
