class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        total = 0
        left  = 0
        shortest = len(nums) + 1

        for i, num in enumerate(nums):
            total += num

            while total - nums[left] >= target:
                total -= nums[left]
                left += 1

            if total >= target:
                shortest = min(shortest, i - left + 1)
        
        return shortest if shortest <= len(nums) else 0
        