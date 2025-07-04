from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ret_ary = [0] * n

        left = 1
        for i in range(n):
            ret_ary[i] = left
            left *= nums[i]

        right = 1
        for i in range(n - 1, -1, -1):
            ret_ary[i] *= right
            right *= nums[i]

        return ret_ary
