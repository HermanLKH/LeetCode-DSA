class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit, minPrice = 0, prices[0]

        for price in prices:
            profit = max(profit, price - minPrice)

            minPrice = min(price, minPrice)

        return profit