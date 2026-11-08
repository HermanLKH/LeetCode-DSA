# Time complexity:  O(N) => O(S + P)
# Space complexity: O(N) => O(S)
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # Time complexity:  O(S), S = number of chars in s
        # Space complexity: O(S)
        words = s.split(' ')

        if len(pattern) != len(words):
            return False

        # Space complexity: O(1), at most 26 pattern, word key-pairs
        lookup = {}
        # Space complexity: O(1), at most 26 words
        seen   = set()

        # Time complexity: O(P + S)
        for p, w in zip(pattern, words):
            if p not in lookup:
                if w in seen:
                    return False
        
                lookup[p] = w
                seen.add(w)

            elif lookup[p] != w:
                return False
            
        return True
