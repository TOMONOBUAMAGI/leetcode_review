from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """Check whether two binary trees are identical.

        Two binary trees are considered the same if they are structurally identical
        and the nodes have the same values.

        Args:
            p (Optional[TreeNode]): The root node of the first tree.
            q (Optional[TreeNode]): The root node of the second tree.

        Returns:
            bool: True if both trees are identical, otherwise False.
        """
        if not p and not q:
            return True

        if (not p and q) or (p and not q) or (p.val != q.val):
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
