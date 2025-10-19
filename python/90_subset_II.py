from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """Generates all possible subsets of a list of integers, avoiding duplicates.

        This function returns the power set of the given list of integers,
        where duplicate subsets are removed by sorting the input and skipping
        duplicate elements during recursion.

        Args:
            nums (List[int]): A list of integers that may contain duplicates.

        Returns:
            List[List[int]]: A list containing all unique subsets of the input list.
        """
        nums.sort()
        answer = []

        def backtrack(subset, idx):
            answer.append(subset)
            for i in range(idx + 1, len(nums)):
                if i != idx + 1 and nums[i] == nums[i - 1]:
                    continue
                next_subset = subset + [nums[i]]
                backtrack(next_subset, i)

        backtrack([], -1)
        return answer
