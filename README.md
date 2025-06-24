# DynamicReasoning

This repository demonstrates two customer service agents that can be compared on KPIs like task completion rate and turns to resolution.

1. **Static Agent** – intent based workflow with predefined responses.
2. **Dynamic Reasoning Agent** – uses a small reasoning engine backed by a knowledge graph.

## Repository Layout

- `static_agent/` – rule-based components and the `StaticAgent` class.
- `dynamic_agent/` – reasoning engine, knowledge graph and the `DynamicAgent` class.
- `common/` – shared utilities such as the placeholder `APIClient`.
- `docs/` – additional documentation and architecture diagrams.
- `tests/` – unit tests for the modules.

Run the tests with:

```bash
pytest
```
