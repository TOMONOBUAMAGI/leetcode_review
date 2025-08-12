from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """Remove the N-th node from the end of a singly linked list.

        This method removes the N-th node from the end of the list and returns
        the head of the modified linked list. It uses a two-pointer approach:
        the first pointer (`former`) is advanced N steps ahead, and then both
        pointers move together until the first pointer reaches the end. The
        second pointer (`latter`) will be just before the node to remove.

        Args:
            head (Optional[ListNode]): The head node of the singly linked list.
            n (int): The position (1-indexed) from the end of the list of the node to remove.

        Returns:
            Optional[ListNode]: The head node of the updated linked list, or None if the list becomes empty.

        Example:
            >>> # Input: 1 -> 2 -> 3 -> 4 -> 5, n = 2
            >>> # Output: 1 -> 2 -> 3 -> 5
        """
        former, latter = head, head
        for _ in range(n):
            former = former.next

        if not former:
            return head.next

        while former.next:
            former = former.next
            latter = latter.next

        latter.next = latter.next.next

        return head
