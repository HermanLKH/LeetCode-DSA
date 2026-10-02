class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        seen = {}
        res = []

        for n in nums1:
            if not seen.get(n):
                seen[n] = 1
        
        for n in nums2:
            if seen.get(n) and n not in res:
                res.append(n)

        return res
