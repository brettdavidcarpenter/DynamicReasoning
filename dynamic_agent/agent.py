from .knowledge_graph import KnowledgeGraph
from .reasoning_engine import ReasoningEngine
from common.api import APIClient


class DynamicAgent:
    """Agent with simple reasoning using a knowledge graph."""

    def __init__(self, knowledge_graph: KnowledgeGraph | None = None, api_client: APIClient | None = None) -> None:
        self.kg = knowledge_graph or KnowledgeGraph()
        self.engine = ReasoningEngine(self.kg)
        self.api = api_client or APIClient()

    def handle(self, text: str) -> str:
        """Generate a response using a reasoning plan."""
        plan = self.engine.plan(text)
        lower_plan = plan.lower()
        if "cancel subscription" in lower_plan:
            self.kg.add_fact("subscription", "cancelled")
            self.api.cancel_subscription("user")
            return "Sure, I've canceled your subscription."
        if "initiate refund" in lower_plan:
            self.kg.add_fact("refund_status", "requested")
            self.api.request_refund("user", "order")
            return "I've submitted a refund request."
        if "confirm cancellation" in lower_plan:
            return "Your subscription is already canceled."
        return "Could you clarify your request?"
