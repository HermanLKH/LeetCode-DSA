class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        matched = {}
        used = set()

        for ch, target in zip(s, t):
            if ch not in matched:
                if target not in used:
                    matched[ch] = target
                    used.add(target)
                else:
                    return False                
            
            replaced_ch = matched[ch]

            if replaced_ch == target:
                continue
            else:
                return False

        return True
        