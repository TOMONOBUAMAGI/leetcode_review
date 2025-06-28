from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_hash = {}
        for index, num in enumerate(nums):
            if num in num_hash:
                print(num_hash)
                return [index, num_hash[num]]
            else:
                num_hash[target - num] = index
