class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        cnt  = 1
        cand = nums[0]

        for num in nums[1:]:
            if cnt == 0:
                cand = num

            if num == cand:
                cnt += 1
            else:
                cnt -= 1

        return cand
        