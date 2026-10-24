# Time complexity:  O(N)
# Space complexity: O(N)
class Solution:
    def minSubarray(self, nums: list[int], p: int) -> int:
        # Time complexity: O(N)
        remainder = sum(nums) % p

        if remainder == 0:
            return 0

        rRemainder = 0
        lookup = {0: -1}
        res = len(nums)

        # Time complexity: O(N)
        for j, num in enumerate(nums):
            rRemainder = (rRemainder + num) % p
            target     = (rRemainder - remainder) % p

            if target in lookup:
                res = min(res, j - lookup[target])

            lookup[rRemainder] = j

        return -1 if res == len(nums) else res
