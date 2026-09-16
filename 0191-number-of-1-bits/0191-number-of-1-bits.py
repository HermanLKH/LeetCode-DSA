class Solution:
    def hammingWeight(self, n: int) -> int:
        bin_n = bin(n)
        count_one = 0

        for d in bin_n:
            if d == '1':
                count_one += 1

        return count_one