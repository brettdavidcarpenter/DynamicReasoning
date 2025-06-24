class Metrics:
    """Track conversation statistics."""

    def __init__(self):
        self.reset()

    def reset(self):
        self.tasks_completed = 0
        self.turns = 0
        self.errors = 0
        self.csat_scores = []  # placeholder for future CSAT metrics

    def record_turn(self):
        self.turns += 1

    def record_task_completed(self):
        self.tasks_completed += 1

    def record_error(self):
        self.errors += 1

    def record_csat(self, score):
        self.csat_scores.append(score)

    def summary(self):
        avg_csat = None
        if self.csat_scores:
            avg_csat = sum(self.csat_scores) / len(self.csat_scores)
        return {
            "tasks_completed": self.tasks_completed,
            "turns": self.turns,
            "errors": self.errors,
            "avg_csat": avg_csat,
        }
