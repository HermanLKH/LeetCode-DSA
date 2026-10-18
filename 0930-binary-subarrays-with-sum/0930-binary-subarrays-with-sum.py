class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        prefix_sum = res = 0
        lookup = {0: 1}

        for num in nums:
            prefix_sum += num
            diff = prefix_sum - goal

            if diff in lookup:
                res += lookup[diff]

            lookup[prefix_sum] = lookup.get(prefix_sum, 0) + 1

        return res        
