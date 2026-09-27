class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        l, r = 1, max(piles)
        eat_h = 0

        while l < r:
            m = l + (r - l) // 2

            for p in piles:
                if eat_h > h:
                    break
                elif p > m: 
                    eat_h += (p + m - 1) // m
                else:
                    eat_h += 1

            if eat_h <= h:
                r = m
            else:
                l = m + 1

            eat_h = 0
            
        return l