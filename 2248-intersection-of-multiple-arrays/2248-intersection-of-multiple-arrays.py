class Solution:
    def intersection(self, nums: list[list[int]]) -> list[int]:
        common = set(nums[0])

        for arr in nums[1:]:
            common.intersection_update(arr)

            if not common:
                return []

        return sorted(common)