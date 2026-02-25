"""Common comparators for key information evaluation.

This package contains comparators that are shared between the traditional
and ANLS Star evaluation systems. These comparators implement a unified
interface that works with both systems.
"""

from .base import BaseComparator
from .exact import ExactComparator
from .levenshtein import LevenshteinComparator
from .llm import LLMComparator
from .numeric import NumericComparator, NumericExactC
from .semantic import SemanticComparator
from .structured import StructuredModelComparator
from ._embedding_utils import generate_bedrock_embedding

# Import LLMComparator if strands-agents is available
try:
    from .llm import LLMComparator  # noqa: F401

    LLM_AVAILABLE = True
except ImportError:
    LLM_AVAILABLE = False

# Import BERTComparator if evaluate is available
try:
    from .bert import BERTComparator  # noqa: F401

    BERT_AVAILABLE = True
except ImportError:
    BERT_AVAILABLE = False

# Import FuzzyComparator and Fuzz alias only if rapidfuzz is available
try:
    from .fuzzy import (  # noqa: F401
        RAPIDFUZZ_AVAILABLE,
        Fuzz,
        FuzzyComparator,
    )
except ImportError:
    RAPIDFUZZ_AVAILABLE = False


__all__ = [
    "BaseComparator",
    "LevenshteinComparator",
    "NumericComparator",
    "NumericExactC",
    "ExactComparator",
    "StructuredModelComparator",
    "SemanticComparator",
    "generate_bedrock_embedding",
]

# Add LLMComparator to __all__ if available
if LLM_AVAILABLE:
    __all__.append("LLMComparator")

# Add BERTComparator to __all__ if available
if BERT_AVAILABLE:
    __all__.append("BERTComparator")

# Add FuzzyComparator and Fuzz to __all__ if available
if RAPIDFUZZ_AVAILABLE:
    __all__.append("FuzzyComparator")
    __all__.append("Fuzz")
