import heapq
from typing import List


class Solution:
    """
    Solution class to find the k closest points to the origin (0, 0).
    """

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        Find the k closest points to the origin based on Euclidean distance.

        Args:
            points (List[List[int]]): A list of [x, y] coordinates representing points.
            k (int): The number of closest points to return.

        Returns:
            List[List[int]]: The list of k closest points to the origin.
        """
        point_heap = []
        for point in points:
            d = point[0] ** 2 + point[1] ** 2

            if len(point_heap) == k:
                heapq.heappushpop(point_heap, [-d, point])
            else:
                heapq.heappush(point_heap, [-d, point])

        return [point for _, point in point_heap]
