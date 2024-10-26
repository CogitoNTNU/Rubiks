from backend.Solvers.astar.node import Node
from backend.Solvers.astar.helpers import copy
from magiccube import Cube


def test_copy():
    parent = Node(Cube())
    node = Node(Cube(), parent, "R", 0, 1)
    copy_of_node = copy(node)
    assert copy_of_node is not node
