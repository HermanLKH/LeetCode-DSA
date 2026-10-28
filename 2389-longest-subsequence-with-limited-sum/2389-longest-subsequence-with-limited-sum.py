# Time complexity:  O(N log N + M log N)
# Space complexity: O(N + M)
class Solution:
    def answerQueries(self, nums: list[int], queries: list[int]) -> list[int]:
        # Time complexity: N log (N)
        nums.sort()
        r_sum = 0
        # Space complexity: O(N)
        prefix_sum = []

        for num in nums:
            r_sum += num
            prefix_sum.append(r_sum)

        # Space complexity: O(M)
        res = []

        # Time complexity:  O(M log N)
        for q in queries:
            l, r = 0, len(prefix_sum) - 1

            while l <= r:
                m = l + (r - l) // 2

                if prefix_sum[m] <= q:
                    l = m + 1
                else:
                    r = m - 1

            res.append(l)

        return res
                    