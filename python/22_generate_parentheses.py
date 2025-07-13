from typing import List


def parentheses(n: int, s: str, open: int, close: int) -> List[str]:
    """Recursively generates all combinations of well-formed parentheses.

    This helper function builds valid parentheses strings using backtracking.
    It ensures that:
    - We never add more than `n` opening or closing brackets.
    - We never add a closing bracket unless there's a matching opening one.

    Args:
        n (int): Total number of pairs of parentheses to generate.
        s (str): Current state of the parentheses string being built.
        open (int): Number of opening parentheses used so far.
        close (int): Number of closing parentheses used so far.

    Returns:
        List[str]: A list of all valid parentheses strings that can be formed.
    """
    if open == n and close == n:
        return [s]

    if open == n:
        return parentheses(n, s + ")", open, close + 1)
    elif open == close:
        return parentheses(n, s + "(", open + 1, close)
    else:
        return parentheses(n, s + "(", open + 1, close) + parentheses(n, s + ")", open, close + 1)


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """Generates all combinations of well-formed parentheses with `n` pairs.

        Args:
            n (int): Number of pairs of parentheses.

        Returns:
            List[str]: All possible combinations of `n` pairs of well-formed parentheses.

        Example:
            >>> sol = Solution()
            >>> sol.generateParenthesis(3)
            ['((()))', '(()())', '(())()', '()(())', '()()()']
        """
        return parentheses(n, "", 0, 0)
