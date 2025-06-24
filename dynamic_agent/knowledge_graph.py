class KnowledgeGraph:
    """Simplified in-memory knowledge graph."""

    def __init__(self):
        self.facts = {}

    def add_fact(self, key: str, value: str) -> None:
        self.facts[key] = value

    def get_fact(self, key: str) -> str:
        return self.facts.get(key, "")
