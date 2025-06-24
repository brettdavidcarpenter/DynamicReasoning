"""Dynamic agent package providing planning utilities and a simple agent."""
from metrics import Metrics


class DynamicAgent:
    """Simple agent using a dynamic script."""

    def __init__(self, metrics: Metrics):
        self.metrics = metrics

    def converse(self, script):
        """Run through a list of actions.

        `script` is an iterable containing strings. When the string is
        "error" an error is recorded.
        """
        for step in script:
            self.metrics.record_turn()
            if step == "error":
                self.metrics.record_error()
        self.metrics.record_task_completed()
        return self.metrics.summary()


from .knowledge_graph import KnowledgeGraph
from .reasoning_engine import ReasoningEngine

__all__ = [
    "DynamicAgent",
    "KnowledgeGraph",
    "ReasoningEngine",
]
