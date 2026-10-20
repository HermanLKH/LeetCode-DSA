# Time complexity:  O(N)
# Space complexity: O(K)
class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        rModulus, res = 0, 0
        lookup = {0: 1}

        for num in nums:
            rModulus = (rModulus + num) % k

            if rModulus in lookup:
                res += lookup[rModulus]

            lookup[rModulus] = lookup.get(rModulus, 0) + 1
        
        return res
