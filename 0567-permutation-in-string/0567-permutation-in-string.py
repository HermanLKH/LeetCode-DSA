class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        
        if len(s2) < len(s1):
            return False

        s1_lookup = dict.fromkeys(string.ascii_lowercase, 0)
        s2_lookup = dict.fromkeys(string.ascii_lowercase, 0)

        for c in s1:
            s1_lookup[c] += 1

        for i in range(len(s1)):
            c = s2[i]
            s2_lookup[c] += 1

            if s2_lookup == s1_lookup:
                return True

        print(s2_lookup)

        for i in range(len(s1), len(s2)):
            s2_lookup[s2[i]] += 1
            print("add", s2[i])
            s2_lookup[s2[i - len(s1)]] -= 1
            print("remove", s2[i - len(s1)])
            print(s2_lookup)
            
            if s2_lookup == s1_lookup:
                return True

        return False