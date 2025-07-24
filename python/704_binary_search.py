from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """Performs binary search to find the index of the target in a sorted list.

        Given a sorted list `nums`, this function returns the index of `target` using
        binary search. If the `target` is not found, it returns -1.

        Args:
            nums (List[int]): A list of integers sorted in ascending order.
            target (int): The integer value to search for.

        Returns:
            int: The index of `target` in `nums` if found, otherwise -1.

        Example:
            >>> sol = Solution()
            >>> sol.search([-1, 0, 3, 5, 9, 12], 9)
            4
            >>> sol.search([-1, 0, 3, 5, 9, 12], 2)
            -1
        """
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (right + left) // 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1

        return -1
