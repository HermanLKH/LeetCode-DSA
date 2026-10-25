# Time complexity:  O(N)
# Space complexity: O(1)
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        current = 0
        res = float('-inf')

        for num in nums:
            current = max(num, current + num)
            res = max(res, current)

        return res
