# Documentation

This document explains how the knowledge graph and reasoning engine function within the dynamic agent.

## Knowledge Graph

The knowledge graph captures tasks and relationships as triples stored in `graph.yaml`. Each node represents an action or piece of contextual information. Edges denote prerequisites or consequences. When the CLI launches the dynamic agent it loads this file into memory, allowing the reasoning engine to query for possible next steps based on the current state.

## Reasoning Engine

The reasoning engine evaluates the knowledge graph to choose actions dynamically:

1. Parse the current goal and state.
2. Query the graph for nodes whose prerequisites are satisfied.
3. Score candidate actions using heuristics.
4. Execute the best action and update the state.
5. Repeat until the goal is achieved or no actions remain.

This approach lets the agent adapt to failures or new information at runtime. The
`ReasoningEngine` queries the `KnowledgeGraph` for neighboring nodes and uses a
breadth‑first search (BFS) to connect a start entity to a goal entity. Each
traversed edge forms a `(subject, relation, object)` triple in the returned plan.

### Configuring relationships for BFS planning

The optional ``relations`` argument restricts which edge types the BFS explores.
Supplying a set of relation names helps focus the plan on specific connections.

```python
from dynamic_agent.knowledge_graph import KnowledgeGraph
from dynamic_agent.reasoning_engine import ReasoningEngine

kg = KnowledgeGraph()
kg.add_fact("A", "next", "B")
kg.add_fact("B", "blocks", "C")
engine = ReasoningEngine(kg)

# Only follow "next" edges during planning
plan = engine.generate_plan("A", "C", relations={"next"})
```

In this case the ``blocks`` relation is ignored and the plan only contains the
allowed ``next`` edge.

## Running the CLI

Use the CLI to run agents and gather metrics.

```bash
# Static agent
python -m dynamicreasoning.cli run static --turns 3 --output runs/static.json

# Dynamic agent
python -m dynamicreasoning.cli run dynamic --script script.txt --output runs/dynamic.json

# Metrics
python -m dynamicreasoning.cli metrics runs/static.json runs/dynamic.json --output metrics.csv

# Compare results
python -m dynamicreasoning.cli compare metrics.csv
```

Running these commands produces JSON logs and CSV metrics that help evaluate how the dynamic agent performs versus the static one.

## Side-by-Side UI

A minimal graphical interface is provided to compare both agents with the same conversation script.
Run it with:

```bash
python -m ui.side_by_side
```

Enter one step per line and press **Run** to display the metrics for `StaticAgent` and `DynamicAgent` side by side.

## Running Tests

Execute the test suite from the repository root:

```bash
PYTHONPATH=. pytest
```

All tests should pass and the output will contain a summary similar to ``6 passed``. Any failures are reported with stack traces to help diagnose issues.
