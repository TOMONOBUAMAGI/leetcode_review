from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """Returns the number of days to wait for a warmer temperature for each day.

        This method uses a monotonic decreasing stack to efficiently compute, for each day,
        how many days to wait until a warmer temperature. If no warmer temperature occurs
        in the future, the value is 0 for that day.

        Args:
            temperatures (List[int]): A list of daily temperatures.

        Returns:
            List[int]: A list where each index i contains the number of days to wait
                       until a warmer temperature. If no such day exists, the value is 0.

        Example:
            >>> sol = Solution()
            >>> sol.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])
            [1, 1, 4, 2, 1, 1, 0, 0]
        """
        size = len(temperatures)
        if size == 1:
            return [0]

        answer = [0] * size
        t_stack = []
        for i in range(size):
            while t_stack and temperatures[t_stack[-1]] < temperatures[i]:
                idx = t_stack.pop()
                answer[idx] = i - idx

            t_stack.append(i)

        return answer
