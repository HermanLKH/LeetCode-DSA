class Solution:
    def findLHS(self, nums: list[int]) -> int:
        res = 0
        freq = {}

        for i in range(len(nums)):
            freq[nums[i]] = freq.get(nums[i], 0) + 1

        for num in nums:
            if num + 1 in freq:
                res = max(res, freq[num + 1] + freq[num])

        return res
