# Stickler Architecture

This document describes the internal package layout of the `stickler` library, the dependency rules between layers, and how to decide where new code belongs.

## Package Dependency Diagram

Arrows indicate "depends on" (points from consumer to provider):

```
reporting  -->  evaluation  -->  metrics  -->  comparison  -->  model_def  -->  comparators  -->  core
```

Each layer may import from any layer to its **right** (lower). No layer may have **module-level** imports from a layer to its **left** (higher). Cross-layer imports from right-to-left are permitted only inside:

- `TYPE_CHECKING` blocks (for type annotations)
- Function / method bodies (lazy imports at call time)

### Layer Summary

| Layer | Package Path | Purpose |
|---|---|---|
| **core** | `structured_object_evaluator/core/` | Zero-dependency primitives: field config, type resolver, enums, helpers |
| **comparators** | `comparators/` | Strategy-pattern comparator classes and registry |
| **model_def** | `structured_object_evaluator/model_def/` | Model definition: StructuredModel, ComparableField, factory, converters |
| **comparison** | `structured_object_evaluator/comparison/` | Comparison engine, dispatcher, field/list handlers, Hungarian matching |
| **metrics** | `structured_object_evaluator/metrics/` | Confusion matrix, precision/recall/F1, AUROC, aggregate metrics |
| **evaluation** | `structured_object_evaluator/evaluation/` | Public evaluation functions, bulk evaluator, ANLS* trees, format helpers |
| **reporting** | `reporting/` | Text, markdown, and HTML output generation |

### Shared Utilities

| Package | Purpose |
|---|---|
| `algorithms/` | Algorithm implementations (e.g., Hungarian algorithm). No stickler imports. |
| `utils/` | Generic utilities: text normalizers, time helpers, argparser, process evaluation |

## Import Rules

1. **Module-level imports** must only go rightward (toward `core`).
2. **Lazy imports** (inside function bodies) may go leftward when needed to break cycles. This pattern is used in 6 places, documented in the codebase.
3. **`TYPE_CHECKING` imports** may reference any layer for annotation purposes.
4. **Within a layer**, modules may freely import each other at module level.
5. **Relative imports** are preferred within a package; absolute imports are used for cross-package references.

## Backward Compatibility

All original import paths (`stickler.structured_object_evaluator.models.*`, etc.) continue to work via **shim files** at the old locations. Shims emit `DeprecationWarning` pointing to the canonical import path. Shims will be removed in **v0.3.0**.

Example:
```python
# Old path (deprecated, still works):
from stickler.structured_object_evaluator.models.structured_model import StructuredModel

# New canonical path:
from stickler.structured_object_evaluator.model_def.structured_model import StructuredModel

# Public API (unchanged, preferred):
from stickler import StructuredModel
```

## Where Does My Code Go?

Use this decision tree when adding new code:

```
Is it a new comparator (strategy for comparing two values)?
  --> comparators/

Is it a zero-dependency type, enum, or helper used by many layers?
  --> core/

Does it define how a model is structured or created?
  --> model_def/

Does it execute the comparison between two model instances?
  --> comparison/

Does it compute metrics from comparison results?
  --> metrics/

Does it orchestrate a full evaluation (single or bulk)?
  --> evaluation/

Does it format or display results for humans?
  --> reporting/

Is it a generic utility with no stickler-specific logic?
  --> utils/

Is it a standalone algorithm (e.g., Hungarian)?
  --> algorithms/
```

## Public API

The public API is defined in `stickler/__init__.py` (8 names) and `structured_object_evaluator/__init__.py` (13 names). These re-export from canonical locations and **must not change** without a major version bump.

### Top-level (`from stickler import ...`)

- `StructuredModel`, `ComparableField`
- `NonMatchField`, `NonMatchType`
- `compare_structured_models`, `anls_score`, `compare_json`
- `aggregate_from_comparisons`

### Mid-level (`from stickler.structured_object_evaluator import ...`)

All of the above, plus:
- `ScoreNode`, `construct_nested_dict`, `merge_and_calculate_mean`
- `print_confusion_matrix`, `print_confusion_matrix_html`
