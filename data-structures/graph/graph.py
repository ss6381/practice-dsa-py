from collections import deque
from dataclasses import dataclass
from typing import Optional, List, Set


@dataclass
class Node:
    key: int
    adjacent: List[Optional["Node"]]

    def __str__(self):
        result = []
        for edge in self.adjacent:
            result.append(str(edge.key))
        return " ".join(result)

    def __eq__(self, node: Optional["Node"]) -> bool:
        return self.key == node.key

    def adjacent_to(self, to_node):
        if to_node in self.adjacent:
            raise ValueError(
                f"Edge from vertex {self.key} to vertex {to_node.key} already exists."
            )
        self.adjacent.append(to_node)


class DirectedGraph:
    """
    Python has does not have an easy built-in graph implementation.
    Here is a simple implementation of a graph using an adjacency list.
    We only add to_vertex to from_vertex's adjacency list rather than
    creating a bidirectional connection.
    """

    def __init__(self, vertices: Optional[List[Node]] = None):
        if vertices is None:
            vertices = []
        for v in vertices:
            if len(v.adjacent) > 0:
                raise ValueError(
                    "Cannot initialize graph with existing edges. Use add_edge method."
                )
        self.vertices = vertices

    def __str__(self):
        result = []
        for vertex in self.vertices:
            result.append("Vertex " + str(vertex.key) + ": " + str(vertex))
        return "\n".join(result)

    def add_vertex(self, k: int):
        vertex = self.get_node(k)
        if vertex is not None:
            raise ValueError(f"Vertex {k} already exists")
        self.vertices.append(Node(key=k, adjacent=[]))

    def add_edge(self, from_key: int, to_key: int):
        from_node = self.get_node(from_key)
        if from_node is None:
            raise ValueError(f"Vertex {from_key} does not exist.")

        to_node = self.get_node(to_key)
        if to_node is None:
            raise ValueError(f"Vertex {to_key} does not exist.")

        from_node.adjacent_to(to_node)

    def get_node(self, k: int) -> Optional[Node]:
        for node in self.vertices:
            if node.key == k:
                return node
        return None

    def topological_sort(self):
        """
        Topological sort is a linear ordering of the vertices of a directed
        acyclic graph (DAG) such that for every directed edge uv from vertex u to vertex v,
        u comes before v in the ordering.
        """
        visited = set()
        sorted_vertices = []
        for vertex in self.vertices:
            if vertex.key not in visited:
                self.__topological_sort(vertex, visited, sorted_vertices)
        return sorted_vertices

    def __topological_sort(self, vertex: Node, visited: Set[int], result: List[int]):
        visited.add(vertex.key)
        for adjacent in vertex.adjacent:
            if adjacent.key not in visited:
                self.__topological_sort(adjacent, visited, result)
        result.insert(0, vertex.key)

    def breadth_first_search(self, root: Node):
        result = []
        visited: Set[int] = set()
        q = deque([root])
        while q:
            curr: Node = q.popleft()
            if curr.key not in visited:
                result.append(curr.key)
                visited.add(curr.key)
                for adjacent in curr.adjacent:
                    q.append(adjacent)
        return result

    def depth_first_search_iterative(self, root: Node):
        result = []
        visited: Set[int] = set()
        stack = [root]
        while stack:
            curr: Node = stack.pop()
            if curr.key not in visited:
                result.append(curr.key)
                visited.add(curr.key)
                for adjacent in curr.adjacent:
                    stack.append(adjacent)
        return result

    def depth_first_search(
        self, node: Optional[Node], visited: Set[int] = set(), result: List[int] = []
    ):
        if not node:
            return result
        result.append(node.key)
        visited.add(node.key)
        for adjacent in node.adjacent:
            if adjacent.key not in visited:
                self.depth_first_search(adjacent, visited, result)
        return result


# g = DirectedGraph([Node(key=1, adjacent=[])])
# g.add_vertex(3)
# g.add_edge(3, 1)
# print(g)
