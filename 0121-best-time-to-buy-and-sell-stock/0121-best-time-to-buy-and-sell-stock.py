class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit, buyPrice = 0, prices[0]

        for price in prices[1:]:
            profit = max(profit, price - buyPrice)

            buyPrice = min(price, buyPrice)

        return profit