"""Backward-compatibility shim. Import from stickler.structured_object_evaluator.evaluation.anls instead."""

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
