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


def test_plan_wrapper():
    kg = KnowledgeGraph()
    kg.add_fact('A', 'next', 'B')
    engine = ReasoningEngine(kg)
    assert engine.plan('A', 'B') == engine.generate_plan('A', 'B')


def test_max_depth_limit():
    kg = KnowledgeGraph()
    kg.add_fact('A', 'r', 'B')
    kg.add_fact('B', 'r', 'C')
    engine = ReasoningEngine(kg)
    # Depth limit of 1 should not reach C
    assert engine.generate_plan('A', 'C', max_depth=1) == []
