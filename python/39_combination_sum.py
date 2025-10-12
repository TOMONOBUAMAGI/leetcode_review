from typing import List


class Solution:
    """
    A class that finds all unique combinations of numbers that sum up to a given target.
    """

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Return all unique combinations of candidates where the chosen numbers sum to `target`.

        The same number may be chosen multiple times, and the order of numbers in each combination does not matter.

        Args:
            candidates (List[int]): A list of positive integers.
            target (int): The target sum to achieve.

        Returns:
            List[List[int]]: A list of all unique combinations that sum to `target`.
        """
        answer = []

        def backtrack(nums, total, idx):
            if total > target or idx == len(candidates):
                return

            if total == target:
                answer.append(nums[:])
                return

            nums.append(candidates[idx])
            backtrack(nums, total + candidates[idx], idx)
            nums.pop()
            backtrack(nums, total, idx + 1)

        backtrack([], 0, 0)
        return answer
