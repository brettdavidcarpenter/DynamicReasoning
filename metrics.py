class Metrics:
    """Track conversation statistics."""

    def __init__(self):
        self.reset()

    def reset(self):
        import time

        self.start_time = time.time()
        self.tasks_completed = 0
        self.turns = 0
        self.errors = 0
        self.csat_scores = []  # placeholder for future CSAT metrics
        self.events = []

    def record_turn(self):
        self.turns += 1
        self.log_event({"type": "turn", "count": self.turns})

    def record_task_completed(self):
        self.tasks_completed += 1
        self.log_event({"type": "task_completed"})

    def record_error(self):
        self.errors += 1
        self.log_event({"type": "error"})

    def record_csat(self, score):
        self.csat_scores.append(score)
        self.log_event({"type": "csat", "value": score})

    def log_event(self, event: dict):
        """Record an arbitrary event in the conversation log."""
        self.events.append(event)

    def summary(self):
        import time

        avg_csat = None
        if self.csat_scores:
            avg_csat = sum(self.csat_scores) / len(self.csat_scores)
        elapsed = time.time() - self.start_time
        success_rate = None
        completed_or_errors = self.tasks_completed + self.errors
        if completed_or_errors:
            success_rate = self.tasks_completed / completed_or_errors
        return {
            "tasks_completed": self.tasks_completed,
            "turns": self.turns,
            "errors": self.errors,
            "avg_csat": avg_csat,
            "elapsed_time": elapsed,
            "success_rate": success_rate,
            "events": list(self.events),
        }
