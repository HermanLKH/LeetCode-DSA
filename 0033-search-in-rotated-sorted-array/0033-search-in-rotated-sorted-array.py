class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + (r - l) // 2

            if nums[m] == target:
                return m
            
            # if left segment sorted
            if nums[l] <= nums[m]:
                # if within left segment
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            # if right segment sorted
            else:
                # if within right segment
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        
        return -1         
