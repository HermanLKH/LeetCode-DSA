class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(' ')

        if len(pattern) != len(words):
            return False

        lookup = {}
        seen   = set()

        for p, w in zip(pattern, words):
            if p not in lookup:
                if w in seen:
                    return False
                else:
                    lookup[p] = w
                    seen.add(w)
            elif lookup[p] != w:
                return False
        return True