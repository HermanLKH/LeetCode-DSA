class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        if len(s) <= 10:
            return []
        
        seen, res = set(), set()
        repeated  = set()
        dna_map   = {'A': 0b00, 'C': 0b01, 'G': 0b10, 'T': 0b11}
        mask      = (1 << 20) - 1
        window    = 0

        for i in range(10):
            window = (window << 2) | dna_map[s[i]]

        seen.add(window)

        for i in range(10, len(s)):
            window = ((window << 2) | dna_map[s[i]]) & mask

            if window in seen and window not in repeated:
                repeated.add(window)
                res.add(s[i - 9:i + 1])
            else:
                seen.add(window)

        return list(res)

        # seen = set()
        # res = set()

        # for i in range(len(s) - 9):
        #     window = s[i:i + 10]

        #     if window in seen:
        #         res.add(window)
        #     else:
        #         seen.add(window)

        # return list(res)
