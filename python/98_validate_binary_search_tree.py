from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """Check whether a binary tree is a valid Binary Search Tree (BST).

        A valid BST is defined as:
        - The left subtree of a node contains only nodes with values less than the node's value.
        - The right subtree of a node contains only nodes with values greater than the node's value.
        - Both the left and right subtrees must also be valid BSTs.

        Args:
            root (Optional[TreeNode]): The root node of the binary tree.

        Returns:
            bool: True if the tree is a valid BST, otherwise False.
        """
        values = []

        def check_val(node):
            if not node:
                return

            check_val(node.left)
            values.append(node.val)
            check_val(node.right)

        check_val(root)
        for i in range(1, len(values)):
            if values[i - 1] >= values[i]:
                return False

        return True
