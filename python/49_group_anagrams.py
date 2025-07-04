from typing import List


def char_nums(s: str) -> str:
    """Generates a key representing the character frequency of the input string.

    This function counts the frequency of each lowercase English letter in the
    input string `s` and returns a comma-separated string representing the counts.
    The result is used as a hashable key to group anagrams.

    Args:
        s (str): A string consisting of lowercase English letters.

    Returns:
        str: A comma-separated string of 26 integers representing the character counts.

    Example:
        >>> char_nums("eat")
        '1,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0'
    """
    char_list = [0 for _ in range(26)]
    for c in s:
        char_list[ord(c) - ord("a")] += 1

    return ",".join(str(x) for x in char_list)


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """Groups a list of strings into anagram groups.

        Each group contains strings that are anagrams of each other.
        An anagram is formed by rearranging the letters of a word to produce a new word.

        Args:
            strs (List[str]): A list of lowercase English words.

        Returns:
            List[List[str]]: A list of groups, where each group is a list of anagram strings.

        Example:
            >>> sol = Solution()
            >>> sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
            [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
        """
        if len(strs) == 1:
            return [strs]

        group_dict = {}
        for s in strs:
            s_char_nums = char_nums(s)
            if s_char_nums in group_dict:
                group_dict[s_char_nums].append(s)
            else:
                group_dict[s_char_nums] = [s]

        return list(group_dict.values())
