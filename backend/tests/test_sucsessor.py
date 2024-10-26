from backend.Solvers.astar.node import Node
from backend.Solvers.astar.helpers import reconstruct_path


def test_node_parent():
    node1 = Node(None, None, "R", 0)
    node2 = Node(None, node1, "L", 1)
    node3 = Node(None, node2, "U", 2)
    node4 = Node(None, node3, "R", 3)
    node5 = Node(None, node4, "U", 4)
    node6 = Node(None, node5, "L", 5)

    assert len(reconstruct_path(node1)) == 1


def test_node_with_one_parent():
    node1 = Node(None, None, "R", 0)
    node2 = Node(None, node1, "L", 1)
    node3 = Node(None, node2, "U", 2)
    node4 = Node(None, node3, "R", 3)
    node5 = Node(None, node4, "U", 4)
    node6 = Node(None, node5, "L", 5)
    assert len(reconstruct_path(node2)) == 2


def test_node_with_five_parent():
    node1 = Node(None, None, "R", 0)
    node2 = Node(None, node1, "L", 1)
    node3 = Node(None, node2, "U", 2)
    node4 = Node(None, node3, "R", 3)
    node5 = Node(None, node4, "U", 4)
    node6 = Node(None, node5, "L", 5)
    assert len(reconstruct_path(node6)) == 6
    path = reconstruct_path(node6)
    assert path[0][1] == node1
