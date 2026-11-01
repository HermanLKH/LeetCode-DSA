class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        if len(s) <= 10:
            return []
        
        dna_map   = {'A': 0b00, 'C': 0b01, 'G': 0b10, 'T': 0b11}
        seen      = bytearray(1 << 20)
        mask      = (1 << 20) - 1
        res       = []
        window    = 0

        for i in range(10):
            window = (window << 2) | dna_map[s[i]]

        seen[window] = 1

        for i in range(10, len(s)):
            window = ((window << 2) | dna_map[s[i]]) & mask

            if seen[window] == 0:
                seen[window] = 1
            elif seen[window] == 1:
                res.append(s[i - 9:i + 1])
                seen[window] = 2

        return res

        # seen = set()
        # res = set()

        # for i in range(len(s) - 9):
        #     window = s[i:i + 10]

        #     if window in seen:
        #         res.add(window)
        #     else:
        #         seen.add(window)

        # return list(res)
