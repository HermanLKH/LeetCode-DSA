# Time complexity:  O(M + N), M = number of characters in s1, 
#                             N = number of characters in s2
# Space complexity: O(1)
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        
        if len(s2) < len(s1):
            return False

        # Time complexity:  O(1) => O(26)
        # Space complexity: O(1) => O(26)
        s1_lookup = dict.fromkeys(string.ascii_lowercase, 0)
        s2_lookup = dict.fromkeys(string.ascii_lowercase, 0)

        # Time complexity: O(M)
        for c in s1:
            s1_lookup[c] += 1

        # Time complexity: O(N)
        # ---------------------
        for i in range(len(s1)):
            c = s2[i]
            s2_lookup[c] += 1

        if s2_lookup == s1_lookup:
            return True

        for i in range(len(s1), len(s2)):
            s2_lookup[s2[i]] += 1
            s2_lookup[s2[i - len(s1)]] -= 1
            
            if s2_lookup == s1_lookup:
                return True
        # ---------------------

        return False