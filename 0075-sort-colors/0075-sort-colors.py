# Time complexity:  O(N)
# Space complexity: O(1)
class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return

        l, m, r = 0, 0, len(nums) - 1

        while m <= r:
            if nums[m] == 0:
                temp    = nums[l]
                nums[l] = nums[m]
                nums[m] = temp

                l += 1
                m += 1

            elif nums[m] == 1:
                m += 1

            else:
                temp    = nums[r]
                nums[r] = nums[m]
                nums[m] = temp

                r -= 1
                
            