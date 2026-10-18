class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        window_sum = 0
        l = 0
        shortest = len(nums) + 1

        for r, num in enumerate(nums):
            if num >= target:
                return 1
            
            window_sum += num

            while window_sum - nums[l] >= target:
                window_sum -= nums[l]
                l += 1

            if window_sum >= target:
                shortest = min(shortest, r - l + 1)
        
        return shortest if shortest <= len(nums) else 0
        