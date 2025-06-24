# DynamicReasoning

This repository provides two simple agents demonstrating static and dynamic reasoning approaches. A small command line tool allows you to chat with either agent.

## Installation

No additional dependencies are required. The code runs with the Python standard library (Python 3.8+).

## Usage

Run the CLI to start a conversation with an agent. Choose between the `static` and `dynamic` agents and optionally run a short demo conversation:

```bash
python scripts/cli.py --agent static --demo
```

Omit `--demo` to enter interactive mode:

```bash
python scripts/cli.py --agent dynamic
```

Type `quit` or `exit` to end an interactive session.

