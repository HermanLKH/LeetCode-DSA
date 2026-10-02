class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        seen = {}
        res = []

        for n in nums1:
            seen[n] = seen.get(n, 0) + 1

        for n in nums2:
            if n in seen and seen[n] > 0:
                res.append(n)
                seen[n] -= 1

        return res