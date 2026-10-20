class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        if k <= 1:
            return 0

        l, res = 0, 0
        product = 1

        for r in range(len(nums)):
            product *= nums[r]
            
            while product >= k:
                product //= nums[l]
                l += 1

            res += r - l + 1

        return res
