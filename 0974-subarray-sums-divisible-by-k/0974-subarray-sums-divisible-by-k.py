class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        runningModulus, res = 0, 0
        lookup = {0: 1}

        for num in nums:
            runningModulus += num
            runningModulus %= k

            if runningModulus in lookup:
                res += lookup[runningModulus]

            lookup[runningModulus] = lookup.get(runningModulus, 0) + 1
        
        return res
