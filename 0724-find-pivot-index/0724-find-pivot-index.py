class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        for i in range(len(nums)):
            if sum(nums[0:i]) == sum(nums[i + 1:len(nums)]):
                return i

        return -1
