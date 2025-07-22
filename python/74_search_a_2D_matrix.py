from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """Searches for a target value in a 2D matrix using binary search.

        This function assumes the following about the matrix:
        - Each row is sorted in ascending order.
        - The first integer of each row is greater than the last integer of the previous row.

        The function first performs binary search on the rows to find the potential row
        that could contain the target, and then performs binary search within that row.

        Args:
            matrix (List[List[int]]): 2D list of integers.
            target (int): The integer to search for.

        Returns:
            bool: True if the target is found, False otherwise.

        Example:
            >>> sol = Solution()
            >>> sol.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3)
            True
        """
        while len(matrix) > 1:
            half_row_idx = len(matrix) // 2
            if target < matrix[half_row_idx][0]:
                matrix = matrix[:half_row_idx]
            else:
                matrix = matrix[half_row_idx:]

        column = matrix[0]
        while column:
            half_column_idx = len(column) // 2
            if target == column[half_column_idx]:
                return True
            elif target > column[half_column_idx]:
                column = column[half_column_idx + 1 :]
            else:
                column = column[:half_column_idx]

        return False
