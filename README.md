# DynamicReasoning

DynamicReasoning demonstrates how a dynamic reasoning engine can outperform a static workflow. The project exposes a command line interface (CLI) that lets you run each agent, collect metrics and compare results.

## Running the CLI

1. Install dependencies

```bash
python -m pip install -r requirements.txt
```

2. Run the static agent

```bash
python -m dynamicreasoning.cli run static --output runs/static.json
```

3. Run the dynamic agent

```bash
python -m dynamicreasoning.cli run dynamic --graph graph.yaml --output runs/dynamic.json
```

## Collecting Metrics

After running the agents, gather metrics with the `metrics` subcommand:

```bash
python -m dynamicreasoning.cli metrics runs/static.json runs/dynamic.json --output metrics.csv
```

## Comparing Agents

Use the `compare` subcommand to display differences between the agents:

```bash
python -m dynamicreasoning.cli compare metrics.csv
```

For additional details including how the knowledge graph and reasoning engine work, see [docs/README.md](docs/README.md).
