"""Backward-compatibility shim. Import from stickler.structured_object_evaluator.core.types instead."""

import warnings as _warnings
_warnings.warn(
    "Import from stickler.structured_object_evaluator.core.types instead. This shim will be removed in v0.3.0.",
    DeprecationWarning,
    stacklevel=2,
)

from ..core.types import (
    TypeResolver,
    _global_resolver,
    get_global_resolver,
    is_list_type,
    is_optional_type,
    register_type,
    resolve_type_string,
)

__all__ = [
    "TypeResolver",
    "_global_resolver",
    "get_global_resolver",
    "register_type",
    "resolve_type_string",
    "is_optional_type",
    "is_list_type",
]
