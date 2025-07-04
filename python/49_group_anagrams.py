from typing import List


def char_nums(s):
    char_list = [0 for _ in range(26)]
    for c in s:
        char_list[ord(c) - ord("a")] += 1

    return ",".join(str(x) for x in char_list)


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
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
