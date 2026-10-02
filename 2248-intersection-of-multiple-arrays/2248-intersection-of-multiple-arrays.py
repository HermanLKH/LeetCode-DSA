class Solution:
    def intersection(self, nums: list[list[int]]) -> list[int]:
        counter = {}
        res = []
        size = len(nums)

        for num in nums:
            for n in num:
                counter[n] = counter.get(n, 0) + 1

        for num, count in counter.items():
            if count == size:
                res.append(num)

        return sorted(res)