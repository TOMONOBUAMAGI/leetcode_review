from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """Detects whether a linked list has a cycle.

        This method uses Floyd's Tortoise and Hare algorithm to determine
        if the given linked list contains a cycle.

        Args:
            head (Optional[ListNode]): The head node of the linked list.

        Returns:
            bool: True if the linked list contains a cycle, False otherwise.
        """
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True

        return False
