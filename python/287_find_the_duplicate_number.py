from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """Find the duplicate number in an array using binary search on value range.

        The input is an array of `n + 1` integers where each integer is between 1 and n
        (inclusive). There is exactly one duplicate number in the array, but it could
        appear multiple times. The task is to find this duplicate without modifying the
        array and using only O(1) extra space.

        Example:
            Input:
                nums = [1, 3, 4, 2, 2]
            Output:
                2

        Algorithm:
            - Apply binary search on the range [1, n].
            - For each mid value, count how many numbers are <= mid.
            - If count > mid, then the duplicate must be in the lower half [left, mid].
            - Otherwise, it lies in the upper half [mid+1, right].
            - Continue until left == right, which will be the duplicate number.

        Args:
            nums (List[int]): List of integers containing n + 1 elements
                with values between 1 and n.

        Returns:
            int: The duplicate number in the array.

        Notes:
            - Time complexity: O(n log n), since for each binary search step
              we perform a linear scan.
            - Space complexity: O(1), no extra data structures used.
        """
        left = 1
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            count = 0
            for num in nums:
                if num <= mid:
                    count += 1

            if count > mid:
                right = mid
            else:
                left = mid + 1

        return left
