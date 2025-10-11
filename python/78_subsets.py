import copy
from typing import List


class Solution:
    """
    A class that generates all possible subsets (the power set) of a given list of numbers.
    """

    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Return all possible subsets of the given list `nums`.

        This implementation iteratively builds subsets by adding each new number
        to all existing subsets.

        Args:
            nums (List[int]): A list of distinct integers.

        Returns:
            List[List[int]]: A list containing all possible subsets of `nums`.
        """
        answer = [[]]
        for num in nums:
            answer_cp = copy.copy(answer)
            for subset in answer_cp:
                answer.append(subset + [num])
        return answer
