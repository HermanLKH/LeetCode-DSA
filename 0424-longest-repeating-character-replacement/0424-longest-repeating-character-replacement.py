class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        left = 0
        longest = 0

        for right, ch in enumerate(s):
            freq[ch] = freq.get(ch, 0) + 1

            while (right - left + 1) - max(freq.values()) > k:
                freq[s[left]] -= 1
                left += 1

            longest = max(longest, right - left + 1)

        return longest
        