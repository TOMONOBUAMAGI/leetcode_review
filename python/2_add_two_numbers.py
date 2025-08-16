from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """Add two numbers represented by linked lists.

        Each linked list stores a non-negative integer in reverse order, where each node
        contains a single digit. The task is to return the sum as a new linked list,
        also in reverse order.

        Example:
            Input:
                l1 = (2 -> 4 -> 3)   # represents 342
                l2 = (5 -> 6 -> 4)   # represents 465
            Output:
                (7 -> 0 -> 8)        # represents 807

        Algorithm:
            - Traverse both linked lists simultaneously.
            - At each step, add corresponding digits and carry from the previous step.
            - Create a new node for the digit (sum % 10).
            - Update carry = sum // 10.
            - Continue until both lists are fully processed and no carry remains.

        Args:
            l1 (Optional[ListNode]): Head of the first linked list.
            l2 (Optional[ListNode]): Head of the second linked list.

        Returns:
            Optional[ListNode]: Head of the resulting linked list representing the sum.

        Notes:
            - Time complexity: O(max(m, n)), where m and n are the lengths of l1 and l2.
            - Space complexity: O(max(m, n)), since a new linked list is created.
        """
        carry_up = 0
        head = ListNode()
        node = head
        while l1 or l2 or carry_up == 1:
            if l1:
                l1_value = l1.val
            else:
                l1_value = 0

            if l2:
                l2_value = l2.val
            else:
                l2_value = 0

            added = l1_value + l2_value + carry_up

            if added >= 10:
                carry_up = 1
                added = added - 10
            else:
                carry_up = 0

            node.next = ListNode(added)

            if l1:
                l1 = l1.next
            else:
                l1 = None

            if l2:
                l2 = l2.next
            else:
                l2 = None

            node = node.next

        return head.next
