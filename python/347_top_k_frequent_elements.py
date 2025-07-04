from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """Finds the k most frequent elements in a list of integers.

        This method counts the frequency of each element in the input list `nums`,
        sorts them by frequency in descending order, and returns the top `k` elements.

        Args:
            nums (List[int]): A list of integers.
            k (int): The number of most frequent elements to return.

        Returns:
            List[int]: A list containing the `k` most frequent elements.

        Example:
            >>> sol = Solution()
            >>> sol.topKFrequent([1, 1, 1, 2, 2, 3], 2)
            [1, 2]
            >>> sol.topKFrequent([1], 1)
            [1]
        """
        if len(nums) == 1:
            return nums

        num_hash = {}

        for num in nums:
            if num in num_hash:
                num_hash[num] += 1
            else:
                num_hash[num] = 1

        sorted_num_hash = sorted(num_hash.items(), key=lambda item: item[1], reverse=True)

        return [freq for freq, _ in sorted_num_hash[:k]]
