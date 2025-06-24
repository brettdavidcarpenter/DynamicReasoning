from dynamic_agent.knowledge_graph import KnowledgeGraph
from dynamic_agent.reasoning_engine import ReasoningEngine


def test_generate_plan_basic():
    kg = KnowledgeGraph()
    kg.add_fact('A', 'next', 'B')
    kg.add_fact('B', 'next', 'C')
    engine = ReasoningEngine(kg)
    plan = engine.generate_plan('A', 'C')
    assert plan == [('A', 'next', 'B'), ('B', 'next', 'C')]


def test_generate_plan_relation_filter():
    kg = KnowledgeGraph()
    kg.add_fact('A', 'r1', 'B')
    kg.add_fact('B', 'r2', 'C')
    engine = ReasoningEngine(kg)
    plan = engine.generate_plan('A', 'C', relations={'r1'})
    assert plan == []
