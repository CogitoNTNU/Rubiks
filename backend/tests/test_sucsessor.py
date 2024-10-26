from backend.Solvers.astar.node import Node
from backend.Solvers.astar.helpers import get_successors


def test_node_parent():
    node1 = Node(None, None, "R", 0)
    node2 = Node(None, node1, "L", 1)
    node3 = Node(None, node2, "U", 2)
    node4 = Node(None, node3, "R", 3)
    node5 = Node(None, node4, "U", 4)
    node6 = Node(None, node5, "L", 5)

    assert len(get_successors(node1) == 1)
    print(get_successors(node6))
