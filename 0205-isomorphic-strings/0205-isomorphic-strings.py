# Time complexity:  O(N)
# Space complexity: O(C), number of unique characters
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        matched = {}
        used = set()

        for ch, target in zip(s, t):
            if ch in matched:
                if matched[ch] != target:
                    return False
            else:
                if target in used:
                    return False

                matched[ch] = target
                used.add(target)

        return True
        