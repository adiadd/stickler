"""Backward-compatibility shim. Import from stickler.comparators.registry instead."""

from stickler.comparators.registry import (
    ComparatorRegistry,
    _global_registry,
    create_comparator,
    get_comparator_class,
    get_global_registry,
    register_comparator,
)

__all__ = [
    "ComparatorRegistry",
    "_global_registry",
    "get_global_registry",
    "register_comparator",
    "get_comparator_class",
    "create_comparator",
]
