class Solution:
    def isValid(self, s: str) -> bool:
        """Determines if the input string of brackets is valid.

        A string is considered valid if all opening brackets are closed
        by the same type of brackets and in the correct order.

        Args:
            s (str): A string consisting only of the characters '(', ')',
                     '{', '}', '[' and ']'.

        Returns:
            bool: True if the string is a valid sequence of brackets,
                  False otherwise.

        Example:
            >>> sol = Solution()
            >>> sol.isValid("()[]{}")
            True
            >>> sol.isValid("(]")
            False
        """
        if len(s) % 2 == 1:
            return False

        brackets_hash = {"[": "]", "(": ")", "{": "}"}
        closing_bracket_stack = []
        for char in s:
            if char in brackets_hash.keys():
                closing_bracket_stack.append(brackets_hash[char])
            else:
                if len(closing_bracket_stack) == 0 or char != closing_bracket_stack.pop():
                    return False

        return len(closing_bracket_stack) == 0
