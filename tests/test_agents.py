import pytest
from dynamic_agent.knowledge_graph import KnowledgeGraph
from static_agent import StaticAgent
from metrics import Metrics


def test_duplicate_cancel_action():
    kg = KnowledgeGraph()
    kg.add_fact('user', 'cancel', 'task1')
    kg.add_fact('user', 'cancel', 'task1')
    assert len(kg.get_facts_by_relation('cancel')) == 1
    assert len(kg) == 1


def test_static_agent_unknown_intent():
    metrics = Metrics()
    agent = StaticAgent(metrics)
    with pytest.raises(AttributeError):
        agent.handle_intent('unknown')
