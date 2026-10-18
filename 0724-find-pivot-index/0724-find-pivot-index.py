# Time complexity:  O(N)
# Space complexity: O(1)
class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        sumLeft = 0
        # Time complexity: O(N)
        sumRight = sum(nums)

        # Time complexity: O(N)
        for i in range(len(nums)):
            sumRight -= nums[i]

            if sumLeft == sumRight:
                return i

            sumLeft += nums[i]

        return -1
