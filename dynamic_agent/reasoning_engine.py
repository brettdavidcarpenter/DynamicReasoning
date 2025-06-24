from .knowledge_graph import KnowledgeGraph


class ReasoningEngine:
    """Very small reasoning engine that consults a knowledge graph."""

    def __init__(self, knowledge_graph: KnowledgeGraph) -> None:
        self.kg = knowledge_graph

    def plan(self, user_input: str) -> str:
        """Return a simple plan string based on input and known facts."""
        text = user_input.lower()
        if "cancel" in text:
            if self.kg.get_fact("subscription") == "cancelled":
                return "Plan: confirm cancellation already completed"
            return "Plan: cancel subscription"
        if "refund" in text:
            return "Plan: initiate refund"
        return "Plan: clarify user request"
