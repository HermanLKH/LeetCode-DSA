class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        l = 0

        while len(nums) >= 3 and nums[-1] + nums[0] + nums[1] > 0:
            nums.pop()

        while len(nums) - l >= 3 and nums[l] + nums[-1] + nums[-2] < 0:
            l += 1

        if len(nums) - l < 3:
            return []

        size = len(nums)
        r = size - 1
        res  = []

        for l in range(size - 2):
            if l > 0 and nums[l] == nums[l - 1]:
                continue

            m = l + 1
            r = size - 1

            while m < r:
                val = nums[l] + nums[m] + nums[r]
                
                if val == 0:
                    res.append([nums[l], nums[m], nums[r]])
                    m += 1
                    r -= 1

                    while m < r and nums[m] == nums[m - 1]:
                        m += 1

                    while m < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif val < 0:
                    m += 1
                else:
                    r -= 1
                
        return res