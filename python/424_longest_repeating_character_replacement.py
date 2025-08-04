class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """Finds the length of the longest substring where up to k characters can be replaced
        to make all characters in the substring the same.

        The function uses a sliding window approach to maintain a window in which
        the number of characters that need to be replaced does not exceed `k`.
        It keeps track of character frequencies within the window and adjusts the
        window size as needed.

        Args:
            s (str): The input string consisting of uppercase English letters.
            k (int): The maximum number of characters that can be replaced.

        Returns:
            int: The length of the longest valid substring after at most `k` replacements.

        Example:
            >>> Solution().characterReplacement("ABAB", 2)
            4
            >>> Solution().characterReplacement("AABABBA", 1)
            4
        """
        left = 0
        char_dict = {}
        answer = 0

        for right in range(len(s)):
            char_dict[s[right]] = char_dict.get(s[right], 0) + 1
            window_width = right - left + 1
            frequent_char_cnt = max(char_dict.values())
            if window_width - frequent_char_cnt > k:
                answer = max(window_width - 1, answer)
                char_dict[s[left]] -= 1
                left += 1

        window_width = right - left + 1
        answer = max(window_width, answer)
        return answer
