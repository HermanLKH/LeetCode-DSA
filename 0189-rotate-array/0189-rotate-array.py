# Time complexity:  O(N)
# Space complexity: O(1)
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k %= len(nums)

        if k == 0:
            return 0

        nums.reverse()
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])

        
        # def reverse(l, r):
        #     while l < r:
        #         nums[l], nums[r] = nums[r], nums[l]
        #         l += 1
        #         r -= 1

        # k %= len(nums)

        # if k == 0:
        #     return 0

        # reverse(0, len(nums) - 1)
        # reverse(0, k - 1)
        # reverse(k, len(nums) - 1)

