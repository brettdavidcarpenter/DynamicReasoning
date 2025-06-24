from static_agent import StaticAgent
from dynamic_agent import DynamicAgent, KnowledgeGraph


def test_static_agent_flow():
    agent = StaticAgent()
    response = agent.handle("please cancel my subscription")
    assert "canceled" in response.lower()


def test_dynamic_agent_uses_kg():
    kg = KnowledgeGraph()
    agent = DynamicAgent(knowledge_graph=kg)
    response = agent.handle("i want a refund")
    assert kg.get_fact("refund_status") == "requested"
    assert "refund" in response.lower()
