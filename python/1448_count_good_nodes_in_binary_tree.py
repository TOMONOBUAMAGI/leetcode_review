from math import inf


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """Counts the number of good nodes in a binary tree.

        A node is considered "good" if on the path from the root to that node,
        there are no nodes with a value greater than the current node's value.

        Args:
            root (TreeNode): The root node of the binary tree.

        Returns:
            int: The total number of good nodes in the tree.
        """
        if not root:
            return 0

        answer = [0]

        def checkGoodness(node: TreeNode, current_max):
            if not node:
                return

            if current_max <= node.val:
                answer[0] += 1
                current_max = node.val

            checkGoodness(node.right, current_max)
            checkGoodness(node.left, current_max)

        checkGoodness(root, -inf)
        return answer[0]
