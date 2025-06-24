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

    def generate_plan(self, start, goal, relations=None, max_depth=None):
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
        max_depth : int or None
            Optional maximum search depth for the plan. ``None`` means no
            depth limit.
        """
        queue = deque([(start, [])])
        visited = {start}
        depth_map = {start: 0}
        while queue:
            node, path = queue.popleft()
            if node == goal:
                return path
            if max_depth is not None and depth_map[node] >= max_depth:
                continue
            for neighbor, rel in self.graph.neighbors(node, relations):
                if neighbor not in visited:
                    visited.add(neighbor)
                    depth_map[neighbor] = depth_map[node] + 1
                    queue.append((neighbor, path + [(node, rel, neighbor)]))
        return []

    # ------------------------------------------------------------------
    # Backwards compatibility -------------------------------------------------
    def plan(self, start, goal, relations=None):
        """Return a plan using :meth:`generate_plan` for compatibility."""
        return self.generate_plan(start, goal, relations)
