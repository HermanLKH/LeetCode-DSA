class Solution:
    def answerQueries(self, nums: list[int], queries: list[int]) -> list[int]:
        # Time complexity: N log (N)
        nums.sort()
        r_sum = 0
        prefix_sum = []

        for num in nums:
            r_sum += num
            prefix_sum.append(r_sum)

        res = []

        for q in queries:
            l, r = 0, len(prefix_sum) - 1

            if q < prefix_sum[l]:
                res.append(0)
                continue

            if q > prefix_sum[r]:
                res.append(r + 1)
                continue

            while l <= r:
                m = l + (r - l) // 2
                num = prefix_sum[m]

                if q == num:
                    res.append(m + 1)
                    break
                elif q > num:
                    l = m + 1
                else:
                    r = m - 1
            else:
                res.append(r + 1)

        return res
                    