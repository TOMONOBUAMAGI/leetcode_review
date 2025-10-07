import heapq
from typing import List


class Solution:
    """
    A class that provides a solution to the "Last Stone Weight" problem
    using a max-heap approach (implemented via negated values in a min-heap).
    """

    def lastStoneWeight(self, stones: List[int]) -> int:
        """
        Simulate the process of repeatedly smashing the two heaviest stones together.
        The result is the weight of the last remaining stone, or 0 if none remain.

        Args:
            stones (List[int]): A list of integers representing the weights of the stones.

        Returns:
            int: The weight of the last remaining stone or 0 if no stones remain.
        """
        for i in range(len(stones)):
            stones[i] = -stones[i]

        heapq.heapify(stones)
        while len(stones) > 1:
            most_heavy = heapq.heappop(stones)
            next_heavy = heapq.heappop(stones)
            new_stone = most_heavy - next_heavy
            if new_stone < 0:
                heapq.heappush(stones, new_stone)

        if stones:
            return -stones[0]
        else:
            return 0
