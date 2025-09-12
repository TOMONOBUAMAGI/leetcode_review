from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """Finds the diameter of a binary tree.

        The diameter is defined as the length of the longest path between
        any two nodes in the tree, which may or may not pass through the root.

        Args:
            root (Optional[TreeNode]): The root node of the binary tree.

        Returns:
            int: The diameter of the binary tree.
        """
        diameter = 0

        def set_diameter(node):
            nonlocal diameter
            if not node:
                return 0

            left_length = set_diameter(node.left)
            right_length = set_diameter(node.right)
            diameter = max(left_length + right_length, diameter)

            return max(left_length, right_length) + 1

        set_diameter(root)

        return diameter
