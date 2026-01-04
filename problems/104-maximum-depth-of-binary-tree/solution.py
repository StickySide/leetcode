# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        def dfs(node: TreeNode | None) -> int:
            return 1 + max(dfs(node.left), dfs(node.right)) if node else 0

        return dfs(root)
