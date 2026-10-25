class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        current = res = float('-inf')

        for num in nums:
            current = max(num, current + num)
            res = max(res, current)

        return res
