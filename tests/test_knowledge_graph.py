import pytest
from dynamic_agent.knowledge_graph import KnowledgeGraph


def test_get_facts_by_entity():
    kg = KnowledgeGraph()
    kg.add_fact('cat', 'is_a', 'animal')
    kg.add_fact('dog', 'is_a', 'animal')
    assert ('cat', 'is_a', 'animal') in kg.get_facts_by_entity('cat')
    facts = kg.get_facts_by_entity('animal')
    assert len(facts) == 2


def test_get_facts_by_relation():
    kg = KnowledgeGraph()
    kg.add_fact('cat', 'likes', 'milk')
    kg.add_fact('dog', 'likes', 'bone')
    facts = kg.get_facts_by_relation('likes')
    assert len(facts) == 2


def test_neighbors():
    kg = KnowledgeGraph()
    kg.add_fact('A', 'r1', 'B')
    kg.add_fact('A', 'r2', 'C')

    # Unfiltered neighbours should include both edges regardless of insertion
    # order.
    assert set(kg.neighbors('A')) == {('B', 'r1'), ('C', 'r2')}

    # Relation filtering should restrict results.
    assert set(kg.neighbors('A', relations={'r1'})) == {('B', 'r1')}

    # Entities without outgoing edges should yield an empty list.
    assert kg.neighbors('D') == []
