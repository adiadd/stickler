"""Backward-compatibility shim. Import from stickler.comparators._embedding_utils instead."""

from ._embedding_utils import generate_bedrock_embedding

__all__ = ["generate_bedrock_embedding"]
