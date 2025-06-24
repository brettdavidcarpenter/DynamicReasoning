import argparse
import json
import csv
import os

from metrics import Metrics
from dynamic_agent import DynamicAgent
from static_agent import StaticAgent


def run_static(args):
    metrics = Metrics()
    agent = StaticAgent(metrics, turns=args.turns)
    summary = agent.converse()
    with open(args.output, "w") as f:
        json.dump(summary, f)


def run_dynamic(args):
    with open(args.script, "r") as f:
        script = [line.strip() for line in f if line.strip()]
    metrics = Metrics()
    agent = DynamicAgent(metrics)
    summary = agent.converse(script)
    with open(args.output, "w") as f:
        json.dump(summary, f)


def compute_metrics(args):
    rows = []
    for path in args.inputs:
        with open(path, "r") as f:
            summary = json.load(f)
        row = {
            "run": os.path.basename(path),
            "tasks_completed": summary.get("tasks_completed"),
            "turns": summary.get("turns"),
            "errors": summary.get("errors"),
            "avg_csat": summary.get("avg_csat"),
        }
        rows.append(row)
    with open(args.output, "w", newline="") as f:
        writer = csv.DictWriter(
            f, fieldnames=["run", "tasks_completed", "turns", "errors", "avg_csat"]
        )
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def compare_metrics(args):
    with open(args.input, "r") as f:
        print(f.read())


def main(argv=None):
    parser = argparse.ArgumentParser(description="Utility CLI for DynamicReasoning")
    subparsers = parser.add_subparsers(dest="command", required=True)

    run_parser = subparsers.add_parser("run", help="Run an agent")
    run_sub = run_parser.add_subparsers(dest="agent", required=True)

    static_parser = run_sub.add_parser("static", help="Run StaticAgent")
    static_parser.add_argument("--turns", type=int, default=1)
    static_parser.add_argument("--output", required=True)
    static_parser.set_defaults(func=run_static)

    dynamic_parser = run_sub.add_parser("dynamic", help="Run DynamicAgent")
    dynamic_parser.add_argument("--script", required=True)
    dynamic_parser.add_argument("--output", required=True)
    dynamic_parser.add_argument("--graph")
    dynamic_parser.set_defaults(func=run_dynamic)

    metrics_parser = subparsers.add_parser(
        "metrics", help="Generate CSV metrics from run summaries"
    )
    metrics_parser.add_argument("inputs", nargs="+")
    metrics_parser.add_argument("--output", required=True)
    metrics_parser.set_defaults(func=compute_metrics)

    compare_parser = subparsers.add_parser("compare", help="Display metrics CSV")
    compare_parser.add_argument("input")
    compare_parser.set_defaults(func=compare_metrics)

    args = parser.parse_args(argv)
    args.func(args)


if __name__ == "__main__":
    main()
