from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """Finds the length of the longest consecutive elements sequence.

        This method finds the length of the longest sequence of consecutive
        integers in the input list `nums`. The solution runs in O(n) time
        complexity by using a set to remove duplicates and to allow O(1) lookups.

        Args:
            nums (List[int]): A list of integers, which may contain duplicates
                and are not necessarily sorted.

        Returns:
            int: The length of the longest consecutive elements sequence.
                 Returns 0 if the input list is empty.

        Example:
            >>> sol = Solution()
            >>> sol.longestConsecutive([100, 4, 200, 1, 3, 2])
            4  # because the longest consecutive sequence is [1, 2, 3, 4]
        """
        if nums == []:
            return 0

        longest = 1
        not_dup_nums = set(nums)
        print(not_dup_nums)

        while not_dup_nums:
            base_num = not_dup_nums.pop()
            length = 1

            num = base_num
            while True:
                num += 1
                if num in not_dup_nums:
                    not_dup_nums.remove(num)
                    length += 1
                else:
                    break

            num = base_num
            while True:
                num -= 1
                if num in not_dup_nums:
                    not_dup_nums.remove(num)
                    length += 1
                else:
                    break

            if length > longest:
                longest = length

            if longest >= len(not_dup_nums):
                return longest
