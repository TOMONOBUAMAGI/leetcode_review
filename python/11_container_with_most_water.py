from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        """Finds the maximum area of water a container can hold.

        This method uses a two-pointer approach to find the two lines that,
        together with the x-axis, form a container that holds the most water.

        Args:
            height (List[int]): A list of non-negative integers representing
                                the height of vertical lines.

        Returns:
            int: The maximum area of water that can be contained.

        Example:
            >>> sol = Solution()
            >>> sol.maxArea([1,8,6,2,5,4,8,3,7])
            49
        """
        left = 0
        right = len(height) - 1
        maximum = min(height[left], height[right]) * (right - left)

        while left < right:
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

            maximum = max(maximum, min(height[left], height[right]) * (right - left))

        return maximum
