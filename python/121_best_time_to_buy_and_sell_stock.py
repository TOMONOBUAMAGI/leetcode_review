from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """Calculates the maximum profit that can be achieved by buying and selling one share of a stock.

        This method assumes you are allowed to buy and sell the stock once.
        The goal is to find the largest difference between a future selling price and a past buying price.

        Args:
            prices (List[int]): A list of daily stock prices, where prices[i] is the price on day i.

        Returns:
            int: The maximum profit achievable. Returns 0 if no profit can be made.

        Example:
            >>> Solution().maxProfit([7, 1, 5, 3, 6, 4])
            5
            >>> Solution().maxProfit([7, 6, 4, 3, 1])
            0
        """
        if len(prices) == 1:
            return 0

        ans = 0
        min_price = prices[0]
        for i in range(1, len(prices)):
            price = prices[i]
            if price < min_price:
                min_price = price
            elif (price - min_price) > ans:
                ans = price - min_price

        return ans
