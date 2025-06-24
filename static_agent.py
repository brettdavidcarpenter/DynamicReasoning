from metrics import Metrics


class StaticAgent:
    """Agent with a static predetermined number of turns."""

    def __init__(self, metrics: Metrics, turns: int = 1):
        self.metrics = metrics
        self.turns = turns

    def converse(self):
        for i in range(self.turns):
            self.metrics.record_turn()
            self.metrics.log_event({"agent": "static", "turn": i + 1})
        self.metrics.record_task_completed()
        return self.metrics.summary()
