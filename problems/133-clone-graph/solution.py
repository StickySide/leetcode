# Definition for a Node.
from __future__ import annotations


class Node:
    def __init__(self, val: int = 0, neighbors: list[Node] | None = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Node | None) -> Node | None:
        map: dict[int, Node] = {}

        def dfs(n: Node):
            # Base case: if node copy already exists, return that node
            if map.get(n.val):
                return map[n.val]

            # If Node copy doesnt exist, make one and return it
            clone = Node(n.val)
            map[n.val] = clone

            # For each neighbor in the node, recursively clone and add to the neighbors of the current node
            for nbr in n.neighbors:
                map[n.val].neighbors.append(dfs(nbr))
            return map[n.val]

        if not node:
            return None
        return dfs(node)
