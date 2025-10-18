from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """Generates all possible permutations of a list of distinct integers.

        Args:
            nums (List[int]): A list of distinct integers.

        Returns:
            List[List[int]]: A list containing all possible permutations of the input list.
        """
        nums.sort()
        answer = []

        def search(ary, remain_nums):
            if len(remain_nums) == 0:
                answer.append(ary[:])
                return

            for i in range(0, len(remain_nums)):
                next_ary = ary + [remain_nums[i]]
                next_remain_nums = remain_nums[:i] + remain_nums[i + 1 :]
                search(next_ary, next_remain_nums)

        search([], nums)
        return answer
