class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        seen = set()
        res = 0
        l = 0

        for r, c in enumerate(s):
            while c in seen:
                seen.remove(s[l])
                l += 1

            seen.add(c)
            res = max(r - l + 1, res)

        return res
