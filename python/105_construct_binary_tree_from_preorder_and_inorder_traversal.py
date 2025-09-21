from collections import deque
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        Reconstruct a binary tree from its preorder and inorder traversal lists.

        Args:
            preorder (List[int]): The preorder traversal of the tree.
            inorder (List[int]): The inorder traversal of the tree.

        Returns:
            Optional[TreeNode]: The root node of the reconstructed binary tree.
        """
        idx_map = {}
        for i in range(len(inorder)):
            idx_map[inorder[i]] = i

        preorder = deque(preorder)

        def build(start, end):
            """
            Recursively build a subtree given the inorder index range.

            Args:
                start (int): Start index of the current subtree in inorder list.
                end (int): End index of the current subtree in inorder list.

            Returns:
                Optional[TreeNode]: The root node of the subtree.
            """
            if start > end:
                return None

            val = preorder.popleft()
            node = TreeNode(val)
            node.left = build(start, idx_map[val] - 1)
            node.right = build(idx_map[val] + 1, end)

            return node

        return build(0, len(preorder) - 1)
