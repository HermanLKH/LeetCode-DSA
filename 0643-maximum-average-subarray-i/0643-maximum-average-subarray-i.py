class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        if len(nums) == k:
            return sum(nums) / k

        l = 0
        window_sum = 0
        max_sum = 0

        for i in range(k):
            window_sum += nums[i]

        max_sum = window_sum

        while len(nums) > l + k:
            window_sum = window_sum - nums[l] + nums[l + k]
            max_sum = max(window_sum, max_sum)

            l += 1

        return max_sum / k
        