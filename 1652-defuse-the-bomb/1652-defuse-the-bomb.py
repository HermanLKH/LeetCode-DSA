class Solution:
    def decrypt(self, code: list[int], k: int) -> list[int]:
        res = [0] * len(code)

        if k == 0:
            return res

        n = len(code)

        if k > 0:
            total = sum(code[1:1 + k])

            for i in range(len(code)):
                res[i] = total
                total -= code[(i + 1) % n]
                total += code[(i + k + 1) % n]
        else:
            total = sum(code[n: n + k - 1: -1])

            for i in range(len(code)):
                res[i] = total
                total -= code[(i + k) % n]
                total += code[i]

        return res