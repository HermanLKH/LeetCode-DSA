class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        sumLeft = 0
        sumRight = sum(nums)

        for i in range(len(nums)):
            if i >= 1:
                sumLeft += nums[i - 1]
                
            sumRight -= nums[i]

            if sumLeft == sumRight:
                return i

        return -1
