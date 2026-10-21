class Solution:
    def minSubarray(self, nums: list[int], p: int) -> int:
        remain = sum(nums) % p

        if remain == 0:
            return 0
        
        res = len(nums)
        curr_remain = 0
        lookup = {0: -1}

        for i, num in enumerate(nums):
            curr_remain = (curr_remain + num) % p
            target = (curr_remain - remain) % p

            if target in lookup:
                res = min(i - lookup[target], res)

            lookup[curr_remain] = i

        return -1 if res == len(nums) else res
