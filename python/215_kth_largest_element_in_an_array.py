import heapq
from typing import List


class Solution:
    """
    Class to solve the problem of finding the k-th largest element in an array.
    """

    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Find the k-th largest element in the array.

        Args:
            nums (List[int]): The input list of integers.
            k (int): The order of the largest element to find.

        Returns:
            int: The k-th largest element.
        """
        queue = [-x for x in nums]
        heapq.heapify(queue)

        for _ in range(k - 1):
            heapq.heappop(queue)

        return -1 * heapq.heappop(queue)
