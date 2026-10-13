class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return

        freq = {0: 0, 1: 0, 2: 0}
        i = 0

        for num in nums:
            freq[num] += 1

        for num in range(3):
            for _ in range(freq[num]):
                nums[i] = num
                i += 1
            