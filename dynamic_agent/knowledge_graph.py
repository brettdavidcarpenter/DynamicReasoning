class KnowledgeGraph:
    """Simple knowledge graph storing facts as (subject, relation, object) triples."""

    def __init__(self):
        self._facts = set()

    def add_fact(self, subject, relation, obj):
        """Add a fact triple to the graph."""
        self._facts.add((subject, relation, obj))

    def get_facts_by_entity(self, entity):
        """Return all facts where the given entity appears as subject or object."""
        return [fact for fact in self._facts if fact[0] == entity or fact[2] == entity]

    def get_facts_by_relation(self, relation):
        """Return all facts with the given relation."""
        return [fact for fact in self._facts if fact[1] == relation]

    def neighbors(self, entity, relations=None):
        """Return neighbors of an entity optionally filtered by relation types.

        Parameters
        ----------
        entity : str
            Entity for which to retrieve neighbors.
        relations : Iterable[str] or None
            If provided, only relations in this collection are considered.
        """
        neighbors = []
        for s, r, o in self._facts:
            if s == entity and (relations is None or r in relations):
                neighbors.append((o, r))
        return neighbors

    def __len__(self):
        return len(self._facts)
