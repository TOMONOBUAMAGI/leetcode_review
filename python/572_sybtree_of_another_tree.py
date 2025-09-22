from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        Determine if `subRoot` is a subtree of `root`.

        Args:
            root (Optional[TreeNode]): The root node of the main tree.
            subRoot (Optional[TreeNode]): The root node of the subtree to check.

        Returns:
            bool: True if `subRoot` is a subtree of `root`, False otherwise.
        """
        if not subRoot:
            return True

        if not root:
            return False

        if self.check(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def check(self, node: Optional[TreeNode], sub_node: Optional[TreeNode]) -> bool:
        """
        Recursively check if two trees are identical.

        Args:
            node (Optional[TreeNode]): The root node of the first tree.
            sub_node (Optional[TreeNode]): The root node of the second tree.

        Returns:
            bool: True if both trees are identical, False otherwise.
        """
        if not node and not sub_node:
            return True

        if node and sub_node and node.val == sub_node.val:
            return self.check(node.left, sub_node.left) and self.check(node.right, sub_node.right)

        return False
