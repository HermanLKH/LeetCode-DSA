class Solution:
    def sumOddLengthSubarrays(self, arr: list[int]) -> int:
        l = 0
        res = 0

        while l <= len(arr) - 1:
            r = l + 1
            res += arr[l]

            while r <= len(arr) - 1:
                if (l + r) % 2 == 0:
                    res += sum(arr[l:r + 1])

                r += 1

            l += 1
            
        return res