# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: "TreeNode", p: "TreeNode", q: "TreeNode") -> "TreeNode":
        """Finds the lowest common ancestor (LCA) of two nodes in a Binary Search Tree (BST).

        The lowest common ancestor is defined as the lowest node in the tree that
        has both `p` and `q` as descendants (a node can be a descendant of itself).

        Args:
            root (TreeNode): The root node of the BST.
            p (TreeNode): The first target node.
            q (TreeNode): The second target node.

        Returns:
            TreeNode: The lowest common ancestor of nodes `p` and `q`.
        """
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root
