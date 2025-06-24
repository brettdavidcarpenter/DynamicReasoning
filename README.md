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

After installing the package you can run the CLI directly:

```bash
pip install -e .
dynamicreasoning run dynamic --script my_script.txt --output out.json
```
The dynamic agent accepts ``--graph`` to load a JSON knowledge graph created
with ``KnowledgeGraph.save``.

## Web UI

A small web interface is provided under `web/`. Start it locally with:

```bash
python web_server.py
```

Then open `http://localhost:8000` in your browser to use the interface. The
same code can be
deployed on Vercel using `api/compare.py` as a serverless function.
