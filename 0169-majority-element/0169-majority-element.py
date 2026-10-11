# Time complexity:  O(N)
# Space complexity: O(1)
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        cnt  = 0

        for num in nums:
            if cnt == 0:
                cand = num

            if num == cand:
                cnt += 1
            else:
                cnt -= 1

        return cand
