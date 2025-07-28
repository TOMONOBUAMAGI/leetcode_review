from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """Searches for a target value in a rotated sorted array.

        This method uses modified binary search to find the index of a given
        target in a rotated sorted array of unique integers. If the target
        does not exist in the array, returns -1.

        Args:
            nums (List[int]): A rotated sorted list of unique integers.
            target (int): The value to search for.

        Returns:
            int: The index of the target if found; otherwise, -1.

        Example:
            >>> sol = Solution()
            >>> sol.search([4, 5, 6, 7, 0, 1, 2], 0)
            4
            >>> sol.search([4, 5, 6, 7, 0, 1, 2], 3)
            -1
        """
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[left] <= nums[mid]:
                if nums[left] <= target and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1
