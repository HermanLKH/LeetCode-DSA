# Time complexity:  O(N)
# Space complexity: O(1)
class Solution:
    def maxScore(self, s: str) -> int:
        # Time complexity: O(N)
        cnt_one = s.count('1')
        cnt_zero = 0
        res = float('-inf')

        # Time complexity: O(N)
        for i in range(len(s) - 1):
            if s[i] == '0':
                cnt_zero += 1
            else:
                cnt_one -= 1

            # Time complexity: O(1)
            res = max(res, cnt_one + cnt_zero)

        return res
