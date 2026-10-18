class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        lookup = {0: 1}
        res = 0

        for num in nums:
            prefix_sum += num
            diff = prefix_sum - k

            if diff in lookup:
                res += lookup[diff]

            lookup[prefix_sum] = lookup.get(prefix_sum, 0) + 1

        return res