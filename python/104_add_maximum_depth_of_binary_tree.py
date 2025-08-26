from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """Calculate the maximum depth of a binary tree.

        The maximum depth is defined as the number of nodes along the longest
        path from the root node down to the farthest leaf node.

        This function uses recursion to compute the depth of the left and
        right subtrees, then returns the larger of the two plus one
        (to account for the current node).

        Args:
            root (Optional[TreeNode]): The root node of the binary tree.
                If None, the depth is 0.

        Returns:
            int: The maximum depth of the binary tree. Returns 0 if the tree is empty.

        Example:
            Given a binary tree:
                    3
                   / \
                  9  20
                     /  \
                    15   7

            maxDepth(root) -> 3
        """
        if not root:
            return 0

        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        return max(left_depth, right_depth) + 1
