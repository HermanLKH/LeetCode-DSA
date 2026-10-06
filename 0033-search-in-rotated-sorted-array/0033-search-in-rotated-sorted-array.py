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
        l, r = 0, pivot - 1
        l2, r2 = pivot, len(nums) - 1
        
        while l <= r:
            m = l + (r - l) // 2

            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1

        while l2 <= r2:
            m = l2 + (r2 - l2) // 2

            if nums[m] == target:
                return m
            elif nums[m] < target:
                l2 = m + 1
            else:
                r2 = m - 1

        return -1         
