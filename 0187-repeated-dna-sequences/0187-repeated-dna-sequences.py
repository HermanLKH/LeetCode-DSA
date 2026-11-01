class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        lookup = {}
        res = []

        for i in range(len(s) - 9):
            dna = s[i:i + 10]

            lookup[dna] = lookup.get(dna, 0) + 1

            if lookup[dna] == 2:
                res.append(dna)

        return res