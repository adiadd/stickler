"""Backward-compatibility shim. Import from stickler.structured_object_evaluator.evaluation.anls instead."""

import warnings as _warnings
_warnings.warn(
    "Import from stickler.structured_object_evaluator.evaluation.anls instead. This shim will be removed in v0.3.0.",
    DeprecationWarning,
    stacklevel=2,
)

from ..evaluation.anls.base import ANLSTree
from ..evaluation.anls.dict_tree import ANLSDict
from ..evaluation.anls.leaf_tree import ANLSLeaf
from ..evaluation.anls.list_tree import ANLSList
from ..evaluation.anls.none_tree import ANLSNone
from ..evaluation.anls.tuple_tree import ANLSTuple

__all__ = [
    "ANLSTree",
    "ANLSDict",
    "ANLSLeaf",
    "ANLSList",
    "ANLSNone",
    "ANLSTuple",
]
