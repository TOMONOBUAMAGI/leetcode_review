class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """Returns the length of the longest substring without repeating characters.

        This method uses a sliding window to keep track of the current substring
        without duplicate characters. It dynamically adjusts the window size as it
        iterates through the string.

        Args:
            s (str): The input string.

        Returns:
            int: The length of the longest substring without repeating characters.

        Example:
            >>> Solution().lengthOfLongestSubstring("abcabcbb")
            3
            >>> Solution().lengthOfLongestSubstring("bbbbb")
            1
            >>> Solution().lengthOfLongestSubstring("")
            0
        """
        char_set = set()
        ans = 0
        left = 0
        for c in s:
            while c in char_set:
                char_set.remove(s[left])
                left += 1

            char_set.add(c)
            ans = max(ans, len(char_set))

        return ans
