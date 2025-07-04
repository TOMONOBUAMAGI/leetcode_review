class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_char_num_ary = [0 for _ in range(26)]
        t_char_num_ary = [0 for _ in range(26)]
        for i in range(len(s)):
            s_char_num_ary[ord("a") - ord(s[i])] += 1
            t_char_num_ary[ord("a") - ord(t[i])] += 1

        return s_char_num_ary == t_char_num_ary
