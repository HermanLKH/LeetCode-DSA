class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if k > len(s):
            return 0
        
        freq = Counter(s)

        for ch, cnt in freq.items():
            if cnt < k:
                parts = s.split(ch)
                longest = 0

                for part in parts:
                    longest = max(longest, self.longestSubstring(part, k))

                return longest
        
        return len(s)
        