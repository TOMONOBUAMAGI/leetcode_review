from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """Finds the right side view of a binary tree.

        The right side view contains the values of the nodes that are visible
        when the tree is viewed from the right side.

        Args:
            root (Optional[TreeNode]): The root node of the binary tree.

        Returns:
            List[int]: A list of node values representing the right side view.
        """
        if not root:
            return []

        r_node_view = self.rightSideView(root.right)
        l_node_view = self.rightSideView(root.left)

        answer = [root.val] + r_node_view
        r_len = len(r_node_view)
        l_len = len(l_node_view)
        if r_len < l_len:
            answer += l_node_view[r_len:l_len]

        return answer
