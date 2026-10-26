class Solution:
    def sumOddLengthSubarrays(self, arr: list[int]) -> int:
        res = 0

        for l in range(len(arr)):
            window_sum = 0

            for r in range(l, len(arr)):
                window_sum += arr[r]

                if (l + r) % 2 == 0:
                    res += window_sum
            
        return res