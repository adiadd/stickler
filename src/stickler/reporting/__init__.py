"""Reporting utilities for structured object evaluation results.

Generates human-readable output from evaluation results:

- ``text.py`` -- Terminal-friendly pretty-printing (confusion matrices, results)
- ``markdown.py`` -- MarkdownUtil for markdown-formatted output
- ``html/`` -- Full HTML report generation (EvaluationHTMLReporter)

Depends on: ``evaluation`` (consumes evaluation result dicts)
"""
