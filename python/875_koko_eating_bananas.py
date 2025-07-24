from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """Finds the minimum integer eating speed `k` such that all banana piles can be eaten in `h` hours.

        This function uses binary search to determine the smallest valid `k` where Koko can
        eat all bananas in `h` hours. At each speed `k`, the number of hours required is
        calculated as the sum of `ceil(pile / k)` for all piles.

        Args:
            piles (List[int]): List of integers representing the size of each banana pile.
            h (int): Total number of hours available to eat all the bananas.

        Returns:
            int: The minimum integer value of eating speed `k` such that all bananas are eaten in `h` hours.

        Example:
            >>> sol = Solution()
            >>> sol.minEatingSpeed([3,6,7,11], 8)
            4
        """
        right = max(piles)  # Max possible speed (e.g., eat a whole pile in one hour)
        left = 1  # Min possible speed

        while left < right:
            mid = (right + left) // 2
            # Total hours needed at speed `mid`
            hours = sum(((p - 1) // mid) + 1 for p in piles)

            if hours > h:
                # Need to eat faster
                left = mid + 1
            else:
                # Try to slow down
                right = mid

        return right
