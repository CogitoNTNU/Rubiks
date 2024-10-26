from typing import Any, Callable, Optional

from . import Node


class Frontier:
    """
    The frontier is a priority queue of nodes. The nodes are sorted by it cost.
    """

    def __init__(self, start_pos: Node, heuristic: Callable, is_goal: Callable):
        """Instantiate a frontier object."""
        self.frontier = [start_pos]
        self.heuristic = heuristic

    def get_frontier(self) -> list[Node]:
        """Getter for the frontier"""
        return self.frontier

    def insert(self, position: Node, cost: float = 0):
        """
        Inserts a node into the frontier. The node is inserted in the
        correct position based on its cost and distance towards the goal.
        Args:
            position (Position): The position of the node
            cost (float, optional): The cost to reach the node. Defaults to 0.
        """
        self.frontier.append(Node(position, cost))
        self.frontier.sort(
            reverse=True,
            key=lambda node: node.weight + self.heuristic(node),
        )

    def pop(self):
        """
        Finds the node with the lowest cost in the frontier and returns it.
        As the frontier is sorted, the node with the lowest cost is the last
        """
        node: Node = self.frontier.pop()
        return node.position

    def is_empty(self):
        """Checks if the frontier is empty"""
        return len(self.frontier) == 0


def a_star(
    state_space, start: Node, heuristic: Callable, is_terminal_state: Callable
) -> tuple[list[Node], list[Node]]:
    """
    A* algorithm implementation

    Args:
        state_space: The state space of the problem
        start (Node): The start node
        heuristic (Callable): The heuristic function
        is_terminal_state (Callable): The goal test function
    Returns:
        The path from the start to the goal node or None if no path exists
    """
    raise NotImplementedError("A* algorithm is not implemented.")
