#!/usr/bin/env python3
"""Command line interface to interact with Static or Dynamic agents."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import argparse
from typing import Callable

from dynamic_reasoning import StaticAgent, DynamicAgent


def run_demo(agent) -> None:
    """Run a short demo conversation with the provided agent."""
    demo_messages = [
        "Hello",
        "How are you?",
        "Tell me something interesting",
        "Goodbye",
    ]
    for msg in demo_messages:
        print(f"You: {msg}")
        print(f"Agent: {agent.reply(msg)}")


def run_interactive(agent) -> None:
    """Start an interactive chat loop with the selected agent."""
    print("Type 'quit' or 'exit' to end the conversation.")
    while True:
        try:
            msg = input("You: ")
        except EOFError:
            break
        if msg.lower() in {"quit", "exit"}:
            break
        print(f"Agent: {agent.reply(msg)}")


def create_agent(agent_name: str):
    """Factory to create the appropriate agent class."""
    if agent_name == "static":
        return StaticAgent()
    if agent_name == "dynamic":
        return DynamicAgent()
    raise ValueError(f"Unknown agent '{agent_name}'")


def main():
    parser = argparse.ArgumentParser(description="Interact with Static or Dynamic agents")
    parser.add_argument(
        "--agent",
        choices=["static", "dynamic"],
        default="static",
        help="Which agent to use for the conversation",
    )
    parser.add_argument(
        "--demo",
        action="store_true",
        help="Run a short demo conversation instead of interactive mode",
    )
    args = parser.parse_args()

    agent = create_agent(args.agent)

    if args.demo:
        run_demo(agent)
    else:
        run_interactive(agent)


if __name__ == "__main__":
    main()
