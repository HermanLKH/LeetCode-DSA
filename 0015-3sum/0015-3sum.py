class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums = sorted(nums)
        l = 0

        while len(nums) - l >= 3 and nums[l] + nums[-1] + nums[-2] < 0:
            l += 1

        while len(nums) >= 3 and nums[-1] + nums[0] + nums[1] > 0:
            nums.pop()

        if len(nums) - l < 3:
            return []

        size = len(nums)
        r = size - 1
        res  = {}

        while l < size - 2:
            m = l + 1
            r = size - 1

            while m < r:
                val = nums[l] + nums[m] + nums[r]
                
                if val == 0:
                    tri = [nums[l], nums[m], nums[r]]
                    key = (nums[l], nums[m], nums[r])
                    res[key] = tri
                    m += 1
                    r -= 1
                elif val < 0:
                    m += 1
                else:
                    r -= 1
            l += 1

        return list(res.values())