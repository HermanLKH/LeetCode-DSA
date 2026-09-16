class Solution:
    def hammingWeight(self, n: int) -> int:
        num_ones = 0

        for i in range(32):
            if (n >> i & 1):
                num_ones += 1
        
        return num_ones