from typing import List


def calc(second: int, first: int, symbol: str) -> int:
    """Performs a basic arithmetic operation between two operands.

    Args:
        second (int): The second operand (top of the stack).
        first (int): The first operand (next on the stack).
        symbol (str): An arithmetic operator: '+', '-', '*', or '/'.

    Returns:
        int: The result of applying the operator to the operands.
             Division truncates toward zero.
    """
    if symbol == "+":
        return first + second
    elif symbol == "-":
        return first - second
    elif symbol == "*":
        return first * second
    else:
        return int(first / second)  # Truncate toward zero


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """Evaluates the value of an arithmetic expression in Reverse Polish Notation (RPN).

        Uses a stack to process the input tokens, applying operations in the correct order.
        The valid operators are '+', '-', '*', and '/'. Each operand is assumed to be an integer.
        Division should truncate toward zero (i.e., like integer division in most programming languages).

        Args:
            tokens (List[str]): A list of tokens representing a valid RPN expression.

        Returns:
            int: The result of evaluating the RPN expression.

        Example:
            >>> sol = Solution()
            >>> sol.evalRPN(["2", "1", "+", "3", "*"])
            9
            >>> sol.evalRPN(["4", "13", "5", "/", "+"])
            6
            >>> sol.evalRPN(["10"])
            10
        """
        if len(tokens) == 1:
            return int(tokens[0])

        num_stack = []
        for token in tokens:
            if token not in ["+", "-", "*", "/"]:
                num_stack.append(int(token))
            else:
                second = num_stack.pop()
                first = num_stack.pop()
                result = calc(second, first, token)
                num_stack.append(result)

        return num_stack[0]
