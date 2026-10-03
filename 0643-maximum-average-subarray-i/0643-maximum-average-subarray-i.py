class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        if len(nums) == k:
            return sum(nums) / k
            
        window_sum = 0

        for i in range(k):
            window_sum += nums[i]

        max_sum = window_sum
        
        for r in range(k, len(nums)):
            window_sum = window_sum - nums[r - k] + nums[r]
            max_sum = max(window_sum, max_sum)

        return max_sum / k
        