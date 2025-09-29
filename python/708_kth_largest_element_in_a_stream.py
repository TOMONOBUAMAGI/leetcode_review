import heapq
from typing import List


class KthLargest:
    """
    Class to maintain the k-th largest element in a dynamic stream of integers.
    """

    def __init__(self, k: int, nums: List[int]):
        """
        Initialize the data structure with a stream of numbers and limit.

        Args:
            k (int): The k-th largest element to maintain.
            nums (List[int]): The initial list of numbers.
        """
        self.limit = k
        self.scores = nums
        heapq.heapify(self.scores)

        # Keep only k largest elements in the min-heap
        while len(self.scores) > self.limit:
            heapq.heappop(self.scores)

    def add(self, val: int) -> int:
        """
        Add a new value to the stream and return the k-th largest element.

        Args:
            val (int): The new value to insert.

        Returns:
            int: The current k-th largest element.
        """
        scores = self.scores
        heapq.heappush(scores, val)

        # Ensure heap size does not exceed limit
        if len(scores) > self.limit:
            heapq.heappop(scores)

        # The smallest element in the heap is the k-th largest overall
        return self.scores[0]
