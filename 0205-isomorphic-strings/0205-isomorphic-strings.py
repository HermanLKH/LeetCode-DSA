class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        matched = {}
        duplicated = {}

        for i, ch in enumerate(s):
            if ch not in matched:
                if t[i] not in duplicated:
                    matched[ch] = t[i]
                    duplicated[t[i]] = 1
                else:
                    return False                
            
            replaced_ch = matched[ch]

            if replaced_ch == t[i]:
                continue
            else:
                return False

        return True
        