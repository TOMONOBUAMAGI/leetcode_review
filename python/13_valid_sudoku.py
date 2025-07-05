from typing import List


def check_validation(nums):
    """Check if a list of Sudoku values contains no duplicates excluding '.'.

    Args:
        nums (List[str]): A list of Sudoku cell values (digits or '.').

    Returns:
        bool: True if no duplicate digits (excluding '.'), False otherwise.
    """
    filtered = [x for x in nums if x != "."]
    return len(filtered) == len(set(filtered))


class Solution:
    """Provides a method to validate a 9x9 Sudoku board."""

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """Determine if a given 9x9 Sudoku board is valid.

        A Sudoku board is valid if:
        - Each row contains no duplicate digits (1–9), ignoring '.'.
        - Each column contains no duplicate digits (1–9), ignoring '.'.
        - Each 3x3 sub-box contains no duplicate digits (1–9), ignoring '.'.

        Args:
            board (List[List[str]]):
                A 9x9 2D list representing the Sudoku board.
                Each cell contains a digit '1'-'9' or '.' for empty.

        Returns:
            bool: True if the board is valid, False otherwise.
        """
        for column in board:
            if not check_validation(column):
                return False

        for i in range(9):
            row = [column[i] for column in board]
            if not check_validation(row):
                return False

        for i in range(3):
            columns = board[3 * i : 3 * i + 3]
            for j in range(3):
                box = [num for column in columns for num in column[3 * j : 3 * j + 3]]
                if not check_validation(box):
                    return False

        return True
