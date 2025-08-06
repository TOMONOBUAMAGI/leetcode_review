from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """Checks if s2 contains a permutation of s1 as a substring.

        This function uses a sliding window and character frequency counting
        to efficiently determine if any substring of s2 is a permutation of s1.

        Args:
            s1 (str): The target string whose permutation is to be searched for.
            s2 (str): The string in which to search for a permutation of s1.

        Returns:
            bool: True if any permutation of s1 is a substring of s2, False otherwise.

        Example:
            >>> Solution().checkInclusion("ab", "eidbaooo")
            True
            >>> Solution().checkInclusion("ab", "eidboaoo")
            False
        """
        left = right = 0
        char_cnt = Counter(s1)

        while right < len(s2):
            char_cnt[s2[right]] -= 1
            while char_cnt[s2[right]] < 0:
                char_cnt[s2[left]] += 1
                left += 1

            if right - left + 1 == len(s1):
                return True

            right += 1

        return False
