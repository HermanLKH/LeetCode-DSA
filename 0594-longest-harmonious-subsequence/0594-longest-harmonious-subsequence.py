class Solution:
    def findLHS(self, nums: list[int]) -> int:
        res = 0
        freq = Counter(nums)

        for num in freq:
            if num + 1 in freq:
                res = max(res, freq[num + 1] + freq[num])

        return res
