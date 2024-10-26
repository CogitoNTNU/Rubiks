from backend.Solvers.astar.node import Node
from backend.Solvers.astar.helpers import copy, get_children
from magiccube import Cube


def test_copy():
    parent = Node(Cube())
    node = Node(Cube(), parent, "R", 0, 1)
    copy_of_node = copy(node)
    assert copy_of_node is not node
    assert copy_of_node.state is not node.state

    assert copy_of_node.parent == node.parent
    assert copy_of_node.action == node.action
    assert copy_of_node.path_cost == node.path_cost

    # Do changes to the original node
    node.state.rotate("R")
    assert copy_of_node.state != node.state


def test_get_children():
    parent = Node(Cube())
    node = Node(Cube(), parent, "R", 0, 1)
    moves = ["R", "L", "U", "D", "F", "B"]
    children = get_children(node, moves)
    assert len(children) == len(moves)
    for child in children:
        assert child.state != node.state
        assert child.parent == node
        assert child.action in moves
        assert child.path_cost == node.path_cost
        assert child.depth == node.depth + 1
        assert child.state.size == node.state.size
