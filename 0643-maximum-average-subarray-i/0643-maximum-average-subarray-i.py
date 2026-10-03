class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        if len(nums) == k:
            return sum(nums) / k

        window_sum = sum(nums[:k])

        max_sum = window_sum
        
        for r in range(k, len(nums)):
            window_sum = window_sum - nums[r - k] + nums[r]
            max_sum = window_sum if window_sum > max_sum else max_sum

        return max_sum / k
        