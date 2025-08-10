from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """Reorders a singly linked list in-place in a specific pattern.

        The list is reordered from:
            L0 → L1 → ... → Ln-1 → Ln
        into:
            L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → ...

        This method:
        1. Finds the midpoint of the list.
        2. Reverses the second half of the list.
        3. Merges the two halves in alternating order.

        The operation modifies the linked list in-place and does not return a value.

        Args:
            head (Optional[ListNode]): The head node of the singly linked list.
                If the list has only one node or is empty, no changes are made.

        Returns:
            None: The list is modified directly.

        Example:
            Given a linked list:
                1 → 2 → 3 → 4 → 5
            After calling reorderList, the list becomes:
                1 → 5 → 2 → 4 → 3
        """
        if head.next is None:
            return

        # 1. Finds the midpoint of the list.
        size = 1
        node = head
        while node.next is not None:
            node = node.next
            size += 1

        center = -(-size // 2)

        # 2. Reverses the second half of the list.
        node = head
        for _ in range(center - 1):
            node = node.next

        latter_head = node.next
        node.next = None
        latter_node = latter_head.next
        latter_head.next = None
        while latter_node is not None:
            next_latter_node = latter_node.next
            latter_node.next = latter_head
            latter_head = latter_node
            latter_node = next_latter_node

        # 3. Merges the two halves in alternating order.
        while latter_head is not None:
            next_head = head.next
            next_latter_head = latter_head.next
            head.next = latter_head
            latter_head.next = next_head
            head = next_head
            latter_head = next_latter_head
