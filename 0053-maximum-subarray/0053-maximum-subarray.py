class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        res = nums[0]
        prefix_sum = 0
        min_prefix = 0

        for num in nums:
            prefix_sum += num
            res = max(res, prefix_sum - min_prefix)
            min_prefix = min(min_prefix, prefix_sum)

        return res
