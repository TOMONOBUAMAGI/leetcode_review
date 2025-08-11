from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """Merge two sorted linked lists into a single sorted linked list.

        This function takes two singly linked lists, each sorted in non-decreasing order,
        and merges them into a single sorted linked list. The merge is performed by
        reusing the nodes of the input lists (i.e., no new nodes are created for the merged list).

        Args:
            list1 (Optional[ListNode]): The head of the first sorted linked list, or None.
            list2 (Optional[ListNode]): The head of the second sorted linked list, or None.

        Returns:
            Optional[ListNode]: The head node of the merged sorted linked list, or None if both input lists are empty.

        Example:
            >>> # list1: 1 -> 3 -> 5
            >>> # list2: 2 -> 4 -> 6
            >>> # merged: 1 -> 2 -> 3 -> 4 -> 5 -> 6
        """
        dummy = node = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                node = list1
                list1 = list1.next
            else:
                node.next = list2
                node = list2
                list2 = list2.next

        if list1 or list2:
            node.next = list1 or list2

        return dummy.next
