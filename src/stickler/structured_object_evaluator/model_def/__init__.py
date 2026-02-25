"""Model definition and creation for structured object evaluation.

Contains the classes that define *what* gets compared:

- ``structured_model.py`` -- StructuredModel base class
- ``comparable_field.py`` -- ComparableField descriptor
- ``factory.py`` -- ModelFactory for dynamic model creation
- ``field_converter.py`` -- FieldConverter and global converter registry
- ``json_schema_converter.py`` -- JsonSchemaFieldConverter
- ``json_schema_validator.py`` -- JSON schema validation utilities
- ``configuration.py`` -- ConfigurationHelper

Depends on: ``core``, ``comparators``
"""
