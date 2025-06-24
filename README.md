# Dynamic Reasoning

This repository contains a toy implementation of two conversational agents:

* **StaticAgent** – executes a fixed number of turns.
* **DynamicAgent** – plans actions using a minimal knowledge graph and reasoning engine.

Both agents report conversation metrics through the `Metrics` helper. A small GUI
lets you compare them side by side.

## Setup

The code requires Python 3.8+ and has no external dependencies. Clone the repo
and run the tests to ensure everything works:

```bash
PYTHONPATH=. pytest
```

For detailed documentation, including how the knowledge graph works and how to
launch the side-by-side UI, see [docs/README.md](docs/README.md).
