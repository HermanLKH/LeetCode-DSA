class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        st = []
        res = prices.copy()

        for i in range(len(prices) - 1, -1, -1):
            price = prices[i]
            
            while st and price < st[-1]:
                st.pop()
            
            if st:
                res[i] -= st[-1]
            
            st.append(price)

        return res