import unittest

from metrics import Metrics
from dynamic_agent import DynamicAgent
from static_agent import StaticAgent


class MetricsTests(unittest.TestCase):
    def test_static_agent_metrics(self):
        metrics = Metrics()
        agent = StaticAgent(metrics, turns=3)
        summary = agent.converse()
        self.assertEqual(summary["turns"], 3)
        self.assertEqual(summary["tasks_completed"], 1)
        self.assertEqual(summary["errors"], 0)
        self.assertIsNone(summary["avg_csat"])
        assert "elapsed_time" in summary
        assert summary["success_rate"] == 1.0

    def test_dynamic_agent_metrics(self):
        metrics = Metrics()
        script = ["msg", "error", "msg"]
        agent = DynamicAgent(metrics)
        summary = agent.converse(script)
        self.assertEqual(summary["turns"], 3)
        self.assertEqual(summary["tasks_completed"], 1)
        self.assertEqual(summary["errors"], 1)
        assert summary["success_rate"] == 0.5


if __name__ == "__main__":
    unittest.main()
