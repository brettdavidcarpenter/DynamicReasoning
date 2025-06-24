from metrics import Metrics
from dynamic_agent import DynamicAgent
from static_agent import StaticAgent


def compare_agents(script_lines):
    """Run both agents on the given script lines."""
    metrics_static = Metrics()
    metrics_dynamic = Metrics()

    dyn_agent = DynamicAgent(metrics_dynamic)
    static_agent = StaticAgent(metrics_static, turns=len(script_lines))

    dynamic_summary = dyn_agent.converse(list(script_lines))
    static_summary = static_agent.converse()

    return {"static": static_summary, "dynamic": dynamic_summary}
