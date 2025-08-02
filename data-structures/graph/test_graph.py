from graph import DirectedGraph, Node
import pytest


"""
Debugging:
1. Test the ad_vertex method separately to confirm that isn't causing the failures.
2. Check the add_edge log around the ValueError to see why the from_node is not found
in the graph's list of vertices.
"""


@pytest.fixture
def graph():
    return DirectedGraph()


def test_graph_init():
    with pytest.raises(
        ValueError,
        match="Cannot initialize graph with existing edges. Use add_edge method.",
    ):
        DirectedGraph([Node(key=1, adjacent=[Node(key=2, adjacent=[])])])


@pytest.mark.parametrize(
    "vertices, expected",
    [
        (
            [2, 6, 3, 7, 1],
            f"Vertex 2: \nVertex 6: \nVertex 3: \nVertex 7: \nVertex 1: ",
        )
    ],
)
def test_graph_add_vertex_success(graph: DirectedGraph, vertices, expected):
    for v in vertices:
        graph.add_vertex(v)
    assert str(graph) == expected


@pytest.mark.parametrize(
    "vertices, error_msg", [([2, 6, 3, 7, 1, 3], "Vertex 3 already exists")]
)
def test_graph_add_vertices_success(graph: DirectedGraph, vertices, error_msg):
    with pytest.raises(ValueError, match=error_msg):
        for v in vertices:
            graph.add_vertex(v)


@pytest.mark.parametrize(
    "vertices, edges, expected",
    [
        (
            [2, 6, 3, 7, 1],
            [(2, 6), (7, 3), (3, 1)],
            f"Vertex 2: 6\nVertex 6: \nVertex 3: 1\nVertex 7: 3\nVertex 1: ",
        ),
    ],
)
def test_graph_add_edge_success(graph: DirectedGraph, vertices, edges, expected):
    for v in vertices:
        graph.add_vertex(v)
    for from_key, to_key in edges:
        graph.add_edge(from_key, to_key)
    assert str(graph) == expected


@pytest.mark.parametrize(
    "vertices, edges, error_msg",
    [
        ([2, 6, 3, 7, 1], [(4, 2)], "Vertex 4 does not exist."),
        ([2, 6, 3, 7, 1], [(2, 5)], "Vertex 5 does not exist."),
        (
            [2, 6, 3, 7, 1],
            [(2, 6), (2, 6)],
            "Edge from vertex 2 to vertex 6 already exists.",
        ),
    ],
)
def test_graph_add_edge_error(graph: DirectedGraph, vertices, edges, error_msg):
    for v in vertices:
        graph.add_vertex(v)
    with pytest.raises(ValueError, match=error_msg):
        for from_key, to_key in edges:
            graph.add_edge(from_key, to_key)


@pytest.mark.parametrize(
    "vertices, edges, expected",
    [
        (
            [0, 1, 2, 3, 4, 5],
            [(5, 2), (5, 0), (2, 3), (3, 1), (4, 0), (4, 1)],
            [5, 4, 2, 3, 1, 0],
        )
    ],
)
def test_topological_sort(graph: DirectedGraph, vertices, edges, expected):
    for v in vertices:
        graph.add_vertex(v)
    for from_key, to_key in edges:
        graph.add_edge(from_key, to_key)
    assert graph.topological_sort() == expected


@pytest.mark.parametrize(
    "vertices, edges, expected",
    [
        (
            [0, 1, 2, 3, 4, 5],
            [(5, 2), (5, 0), (2, 3), (3, 1), (4, 0), (4, 1)],
            [5, 2, 0, 3, 1],
        )
    ],
)
def test_bfs(graph: DirectedGraph, vertices, edges, expected):
    for v in vertices:
        graph.add_vertex(v)
    for from_key, to_key in edges:
        graph.add_edge(from_key, to_key)
    assert graph.breadth_first_search(graph.get_node(5)) == expected


@pytest.mark.parametrize(
    "vertices, edges, expected",
    [
        (
            [0, 1, 2, 3, 4, 5],
            [(5, 2), (5, 0), (2, 3), (3, 1), (4, 0), (4, 1)],
            [5, 2, 3, 1, 0],
        )
    ],
)
def test_dfs(graph: DirectedGraph, vertices, edges, expected):
    for v in vertices:
        graph.add_vertex(v)
    for from_key, to_key in edges:
        graph.add_edge(from_key, to_key)
    assert graph.depth_first_search(graph.get_node(5)) == expected
