from collections import Counter
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """Determines if a word exists in a 2D board by traversing adjacent cells.

        The function checks whether the given word can be formed by sequentially
        adjacent cells (horizontally or vertically). Each cell can be used at most
        once in a single path. The search is optimized by potentially reversing the
        word based on character frequency to reduce backtracking.

        Args:
            board (List[List[str]]): 2D list representing the board of characters.
            word (str): The target word to search for in the board.

        Returns:
            bool: True if the word exists in the board, False otherwise.
        """
        row_num, column_num = len(board), len(board[0])
        visited = set()

        # Optimize search direction by character frequency
        count = Counter(word)
        if count[word[0]] > count[word[-1]]:
            word = word[::-1]

        def search(idx, row, column):
            if (
                not (0 <= row < row_num)
                or not (0 <= column < column_num)
                or word[idx] != board[row][column]
                or (row, column) in visited
            ):
                return False

            if idx == len(word) - 1:
                return True

            visited.add((row, column))
            res = (
                search(idx + 1, row - 1, column)
                or search(idx + 1, row + 1, column)
                or search(idx + 1, row, column - 1)
                or search(idx + 1, row, column + 1)
            )
            visited.remove((row, column))
            return res

        for i in range(row_num):
            for j in range(column_num):
                if search(0, i, j):
                    return True
        return False
