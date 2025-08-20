from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """Solution class for binary tree inversion."""

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """Invert a binary tree by recursively swapping left and right children.

        Args:
            root (Optional[TreeNode]): The root node of the binary tree.

        Returns:
            Optional[TreeNode]: The root of the inverted binary tree.
        """
        if root:
            # Recursively invert left and right subtrees
            self.invertTree(root.left)
            self.invertTree(root.right)
            # Swap the left and right children
            root.left, root.right = root.right, root.left

        return root
