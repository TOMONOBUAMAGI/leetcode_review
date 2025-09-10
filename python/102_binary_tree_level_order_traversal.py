from collections import deque
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """Performs a level-order traversal (breadth-first search) on a binary tree.

        Args:
            root (Optional[TreeNode]): The root node of the binary tree.

        Returns:
            List[List[int]]: A list of lists, where each inner list contains
            the node values at that particular depth level.
        """
        if not root:
            return []

        dq = deque([root])
        answer = []

        # Scan through each traversal
        while len(dq):
            traversal_vals = []

            # Scan each node in a traversal
            for _ in range(len(dq)):
                node = dq.popleft()
                traversal_vals.append(node.val)
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)

            answer.append(traversal_vals)

        return answer
