class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        st = []
        res = prices.copy()

        for i in range(len(prices) - 1, -1, -1):
            while st and prices[i] < prices[st[-1]]:
                st.pop()
            
            if st:
                res[i] -= prices[st[-1]]
            
            st.append(i)
        print(st)
        return res