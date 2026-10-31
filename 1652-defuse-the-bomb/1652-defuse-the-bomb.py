# Time complexity:  O(N)
# Space complexity: O(N)
class Solution:
    def decrypt(self, code: list[int], k: int) -> list[int]:
        n = len(code)
        res = [0] * n

        if k == 0:
            return res
            
        elif k > 0:
            window_sum = sum(code[1:1 + k])

            for i in range(n):
                res[i] = window_sum
                window_sum -= code[(i + 1) % n]
                window_sum += code[(i + k + 1) % n]
        else:
            window_sum = sum(code[k:])

            for i in range(n):
                res[i] = window_sum
                window_sum -= code[(i + k) % n]
                window_sum += code[i]

        return res
