from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        """Finds the minimum element in a rotated sorted array without duplicates.

        The input array is assumed to be originally sorted in ascending order
        and then possibly rotated at some unknown pivot. This function uses
        binary search to locate the minimum element in O(log n) time.

        Args:
            nums (List[int]): A rotated sorted list of unique integers.

        Returns:
            int: The minimum element in the array.

        Raises:
            ValueError: If the input list is empty.

        Example:
            >>> sol = Solution()
            >>> sol.findMin([3, 4, 5, 1, 2])
            1
        """
        if not nums:
            raise ValueError("Input list must not be empty.")

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid - 1] > nums[mid]:
                return nums[mid]
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid - 1

        return nums[left]
