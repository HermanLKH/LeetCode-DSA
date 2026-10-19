class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        if len(nums) <= 1:
            return False

        runningSum = 0
        lookup = {0: -1}

        for i, num in enumerate(nums):
            runningSum = (runningSum + num) % k

            if runningSum in lookup:
                if i - lookup[runningSum] >= 2:
                    return True
            else:
                lookup[runningSum] = i
        
        return False
