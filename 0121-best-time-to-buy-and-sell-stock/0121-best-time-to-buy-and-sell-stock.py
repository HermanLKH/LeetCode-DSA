class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit, buyPrice = 0, prices[0]

        for price in prices[1:]:
            if price < buyPrice:
                buyPrice = price

            profit = max(profit, price - buyPrice)

        return profit