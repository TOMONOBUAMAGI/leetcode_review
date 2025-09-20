from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """Find the k-th smallest element in a Binary Search Tree (BST).

        This uses an in-order traversal, which visits nodes in ascending order
        for a BST. A counter tracks how many nodes have been visited, and the
        traversal stops once the k-th smallest is found.

        Args:
            root (Optional[TreeNode]): The root node of the BST.
            k (int): The k-th position to find (1-indexed).

        Returns:
            int: The value of the k-th smallest node in the BST.
        """
        self.count = 0
        self.answer = None

        def dfs(node):
            if not node or self.answer:
                return

            dfs(node.left)
            self.count += 1
            if self.count == k:
                self.answer = node.val
                return
            dfs(node.right)

        dfs(root)
        return self.answer
