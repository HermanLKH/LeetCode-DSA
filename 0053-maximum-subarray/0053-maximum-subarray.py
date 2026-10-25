class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        current = res = nums[0]

        for i in range(1, len(nums)):
            current = max(nums[i], current + nums[i])
            res = max(res, current)

        return res
