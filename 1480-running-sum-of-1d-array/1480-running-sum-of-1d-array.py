class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        rSum = 0
        res = []

        for num in nums:
            rSum += num
            res.append(rSum)

        return res
