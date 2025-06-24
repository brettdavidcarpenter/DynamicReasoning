class KnowledgeGraph:
    """Simple knowledge graph storing facts and adjacency information."""

    def __init__(self):
        # All facts are stored to allow inspection and searching by tests or
        # other tooling.  Using a ``set`` ensures no duplicate triples are
        # inserted.
        self._facts = set()

        # Adjacency list mapping ``subject -> relation -> set(objects)``.  This
        # structure enables efficient lookup of neighbour entities without having
        # to iterate over all facts on every call.
        self._adj = {}

    # ------------------------------------------------------------------
    # Basic graph manipulation utilities

    def has_fact(self, subject, relation, obj):
        """Return True if the triple exists in the graph."""
        return (subject, relation, obj) in self._facts

    def add_fact(self, subject, relation, obj):
        """Add a fact triple to the graph."""
        if (subject, relation, obj) in self._facts:
            return

        self._facts.add((subject, relation, obj))
        self._adj.setdefault(subject, {}).setdefault(relation, set()).add(obj)

    # ------------------------------------------------------------------
    # Persistence helpers ----------------------------------------------------

    def save(self, path):
        """Serialize the graph to a JSON file."""
        import json

        data = list(self._facts)
        with open(path, "w") as f:
            json.dump(data, f)

    @classmethod
    def load(cls, path):
        """Load a graph from a JSON file and return a new instance."""
        import json

        kg = cls()
        with open(path, "r") as f:
            data = json.load(f)
        for s, r, o in data:
            kg.add_fact(s, r, o)
        return kg

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
        rel_map = self._adj.get(entity, {})
        for rel, objs in rel_map.items():
            if relations is None or rel in relations:
                for obj in objs:
                    neighbors.append((obj, rel))
        return neighbors

    def __len__(self):
        return len(self._facts)
