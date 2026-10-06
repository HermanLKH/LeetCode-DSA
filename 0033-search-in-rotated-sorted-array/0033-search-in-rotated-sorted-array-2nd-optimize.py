class Solution:
    def search(self, nums: list[int], target: int) -> int:
        sorted_nums = []
        l, r = 0, len(nums) - 1

        while l < r:
            m = l + (r - l) // 2

            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        
        pivot = l

        if target > nums[pivot - 1] or target < nums[pivot]:
            return -1
        elif pivot == 0 or target < nums[0]:
            l, r = pivot, len(nums) - 1
        else:
            l, r = 0, pivot - 1
        
        while l <= r:
            m = l + (r - l) // 2

            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1

        return -1         
