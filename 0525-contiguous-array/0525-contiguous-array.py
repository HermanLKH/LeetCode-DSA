class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        longest = 0
        prefix_sum = 0
        lookup = {0: -1}

        for i, num in enumerate(nums):
            prefix_sum += 1 if num == 1 else - 1

            if prefix_sum in lookup:
                longest = max(i - lookup[prefix_sum], longest)
            else:
                lookup[prefix_sum] = i
        
        return longest