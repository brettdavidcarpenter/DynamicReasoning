from collections import deque


class ReasoningEngine:
    """Simple reasoning engine that plans paths between entities using relations.

    Parameters
    ----------
    graph : KnowledgeGraph
        Graph containing entity relationships.
    """

    def __init__(self, graph):
        self.graph = graph

    def generate_plan(self, start, goal, relations=None):
        """Generate a plan (a sequence of triples) from start to goal.

        The engine performs a breadth-first search over the relations in the
        knowledge graph. Optionally a set of relation types can be provided to
        restrict the search.

        Parameters
        ----------
        start : str
            Starting entity.
        goal : str
            Target entity.
        relations : Iterable[str] or None
            Allowed relations to traverse. ``None`` means all relations are
            allowed.
        """
        queue = deque([(start, [])])
        visited = {start}
        while queue:
            node, path = queue.popleft()
            if node == goal:
                return path
            for neighbor, rel in self.graph.neighbors(node, relations):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, path + [(node, rel, neighbor)]))
        return []
