class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if len(s) <= 1:
            return ""
        
        chars = set(s)
        
        for i, ch in enumerate(chars):
            if ch.swapcase() not in chars:
                parts = s.split(ch)
                longest_str = ""

                for part in parts:
                    candidate_str = self.longestNiceSubstring(part)

                    if len(candidate_str) > len(longest_str):
                        longest_str = candidate_str

                return longest_str

        return s