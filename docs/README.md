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

This approach lets the agent adapt to failures or new information at runtime.

## Running the CLI

Use the CLI to run agents and gather metrics.

```bash
# Static agent
python -m dynamicreasoning.cli run static --output runs/static.json

# Dynamic agent
python -m dynamicreasoning.cli run dynamic --graph graph.yaml --output runs/dynamic.json

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
