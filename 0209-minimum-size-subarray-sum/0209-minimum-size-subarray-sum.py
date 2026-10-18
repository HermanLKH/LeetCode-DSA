class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        window_sum = 0
        l = 0
        shortest = float("inf")

        for r, num in enumerate(nums):
            window_sum += num

            while window_sum >= target:
                length = r - l + 1

                if length < shortest:
                    shortest = length

                    if shortest == 1:
                        return 1

                window_sum -= nums[l]
                l += 1
            
        return shortest if shortest != float("inf") else 0
        