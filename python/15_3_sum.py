from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """Finds all unique triplets in the array that sum to zero.

        This method sorts the input list and uses the two-pointer technique
        to efficiently find triplets (i, j, k) such that:
            nums[i] + nums[j] + nums[k] == 0
        Duplicate triplets are not included in the result.

        Args:
            nums (List[int]): A list of integers.

        Returns:
            List[List[int]]: A list of unique triplets [i, j, k] such that
                             nums[i] + nums[j] + nums[k] == 0.

        Example:
            >>> sol = Solution()
            >>> sol.threeSum([-1, 0, 1, 2, -1, -4])
            [[-1, -1, 2], [-1, 0, 1]]
        """
        answer = []
        nums.sort()

        if nums[-1] < 0:  # Early exit: if max < 0, no triple can sum to 0
            return answer

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # Skip duplicate starting elements

            j = i + 1
            k = len(nums) - 1

            while j < k:
                total = nums[i] + nums[j] + nums[k]

                if total > 0:
                    k -= 1
                elif total < 0:
                    j += 1
                else:
                    answer.append([nums[i], nums[j], nums[k]])
                    j += 1
                    # Skip duplicates for second number
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1

        return answer
