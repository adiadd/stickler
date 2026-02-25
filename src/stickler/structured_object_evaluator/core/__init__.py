"""Core domain primitives for structured object evaluation.

This is the lowest layer of the package. It contains zero-dependency types
and helpers that every other layer may import:

- ``field.py`` -- ComparableFieldConfig / ComparisonInfo
- ``types.py`` -- TypeResolver and global type registry
- ``non_match.py`` -- NonMatchField and NonMatchType enums
- ``field_helper.py`` -- FieldHelper
- ``threshold_helper.py`` -- ThresholdHelper
- ``confidence_helper.py`` -- ConfidenceHelper
- ``exceptions.py`` -- SticklerError hierarchy (placeholder)
"""
