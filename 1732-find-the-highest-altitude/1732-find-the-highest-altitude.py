class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        rSum = 0
        res = 0

        for g in gain:
            rSum += g
            res = max(res, rSum)

        return res