from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """Returns an array such that each element at index i is the product
        of all the numbers in the input list except nums[i].

        This implementation does not use division and runs in O(n) time with O(1)
        additional space (excluding the output array). It first calculates prefix
        products (left side) and then suffix products (right side) in two passes.

        Args:
            nums (List[int]): A list of integers.

        Returns:
            List[int]: A list where each element is the product of all elements
                       in the original list except the one at the same index.

        Example:
            >>> sol = Solution()
            >>> sol.productExceptSelf([1, 2, 3, 4])
            [24, 12, 8, 6]
        """
        n = len(nums)
        result = [0] * n

        left = 1
        for i in range(n):
            result[i] = left
            left *= nums[i]

        right = 1
        for i in range(n - 1, -1, -1):
            result[i] *= right
            right *= nums[i]

        return result
