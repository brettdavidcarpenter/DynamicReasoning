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
