from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        """Create a deep copy of a linked list with `next` and `random` pointers.

        Each node in the linked list contains:
            - `val`: the node's value
            - `next`: pointer to the next node
            - `random`: pointer to any node in the list or `None`

        This method returns a deep copy where both `next` and `random` pointers
        in the copied list reference the copied nodes (not the original ones).

        Args:
            head (Optional[Node]): The head node of the original linked list.

        Returns:
            Optional[Node]: The head node of the deep-copied linked list.

        Example:
            Original list:
                Node1(val=7) -> Node2(val=13) -> Node3(val=11)
                Node1.random = None
                Node2.random = Node1
                Node3.random = Node2

            After calling:
                A new list is created with identical structure and values,
                but all nodes are distinct objects from the original.

        Notes:
            - Uses a dictionary to map original nodes to their corresponding copied nodes.
            - Includes a mapping for `None` to avoid extra conditional checks.
        """
        node = head
        node_dict = {None: None}
        while node:
            node_dict[node] = Node(node.val)
            node = node.next

        node = head
        while node:
            cp_node = node_dict[node]
            cp_node.next = node_dict[node.next]
            cp_node.random = node_dict[node.random]
            node = node.next

        return node_dict[head]
