from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """Check whether a binary tree is height-balanced.

        A binary tree is height-balanced if, for every node, the depths of the left
        and right subtrees differ by no more than 1.

        Args:
            root (Optional[TreeNode]): The root node of the binary tree.

        Returns:
            bool: True if the tree is height-balanced, otherwise False.
        """
        if not root:
            return True

        validity = [True]

        def check_depth(node):
            if not node:
                return 0

            right_depth = check_depth(node.right)
            left_depth = check_depth(node.left)
            if abs(right_depth - left_depth) > 1:
                validity[0] = False

            return max(right_depth, left_depth) + 1

        check_depth(root)
        return validity[0]
