"""Comparison orchestration for structured object evaluation.

Contains the engine, dispatcher, and handler classes that execute
field-by-field and list-level comparisons:

- ``engine.py`` -- ComparisonEngine (top-level orchestrator)
- ``dispatcher.py`` -- ComparisonDispatcher
- ``helpers.py`` -- ComparisonHelper (static utilities)
- ``helpers_base.py`` -- ComparisonHelperBase (ABC / template pattern)
- ``hungarian_helper.py`` -- HungarianHelper (optimal list matching)
- ``result.py`` -- ResultHelper
- ``field_handler.py`` -- FieldComparator
- ``primitive_list_handler.py`` -- PrimitiveListComparator
- ``structured_list_handler.py`` -- StructuredListComparator
- ``null_handler.py`` -- NullHelper

Depends on: ``core``, ``comparators``, ``model_def``
"""
