from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """Finds two numbers in a sorted array that add up to the target.

        This method assumes the input array is sorted in non-decreasing order,
        and uses the two-pointer technique to find the pair in O(n) time.

        Args:
            numbers (List[int]): A list of integers sorted in non-decreasing order.
            target (int): The target sum to find.

        Returns:
            List[int]: A list containing the 1-based indices of the two numbers
                       whose sum is equal to the target.

        Example:
            >>> sol = Solution()
            >>> sol.twoSum([2, 7, 11, 15], 9)
            [1, 2]
        """
        left = 0
        right = len(numbers) - 1

        while numbers[left] + numbers[right] != target:
            if numbers[left] + numbers[right] < target:
                left += 1
            else:
                right -= 1

        return [left + 1, right + 1]
