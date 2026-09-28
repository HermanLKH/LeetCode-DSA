class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        l, r = max(weights), sum(weights)

        while l < r:
            m = l + (r - l) // 2

            load, days_needed = 0, 0

            for w in weights:
                if load + w > m:
                    days_needed += 1
                    load = 0
                load += w

            if days_needed < days:
                r = m
            else:
                l = m + 1
        return l