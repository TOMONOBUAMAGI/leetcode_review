from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """Reverses a singly linked list.

        This method iteratively reverses the pointers of a singly linked list
        so that the head becomes the tail and the tail becomes the head.

        Args:
            head (Optional[ListNode]): The head node of the singly linked list.

        Returns:
            Optional[ListNode]: The new head node of the reversed linked list.
            Returns None if the input list is empty.

        Example:
            Given a linked list: 1 -> 2 -> 3 -> None
            The reversed list will be: 3 -> 2 -> 1 -> None
        """
        node = None

        while head:
            head_cp = head
            head = head.next
            head_cp.next = node
            node = head_cp

        return node
