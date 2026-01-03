from __future__ import annotations
from typing import Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """Check if two binary trees are identical using BFS traversal."""

        def traverse(n: Optional[TreeNode]) -> list[int | None]:
            """Serialize tree to list with None for missing nodes."""
            tree: list[int | None] = []
            queue: deque[Optional[TreeNode]] = deque([n])

            while queue:
                node = queue.popleft()
                # Append value or None to capture structure
                tree.append(node.val if node is not None else None)
                # Add children even if None to preserve structure
                if node is not None:
                    queue.append(node.left)
                    queue.append(node.right)
            return tree

        # Compare serialized representations
        return traverse(p) == traverse(q)
