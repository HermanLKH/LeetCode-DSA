class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        seen = set()
        res = 0
        l, r = 0, 0

        while r < len(s):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            else:
                seen.add(s[r])
            
            res = max(r - l + 1, res)
            r += 1

        return res
