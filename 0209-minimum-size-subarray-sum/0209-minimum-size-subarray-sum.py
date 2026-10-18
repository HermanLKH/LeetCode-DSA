class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        total = 0
        l  = 0
        shortest = len(nums) + 1

        for r, num in enumerate(nums):
            if num >= target:
                return 1
                
            total += num

            while total - nums[l] >= target:
                total -= nums[l]
                l += 1

            if total >= target:
                shortest = min(shortest, r - l + 1)

        return shortest if shortest <= len(nums) else 0
        