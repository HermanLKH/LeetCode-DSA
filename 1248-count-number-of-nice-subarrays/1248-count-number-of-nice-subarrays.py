class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        odd_cnt, res = 0, 0
        lookup = {0: 1}

        for num in nums:
            odd_cnt += num % 2

            diff = odd_cnt - k

            if diff in lookup:
                res += lookup[diff]

            lookup[odd_cnt] = lookup.get(odd_cnt, 0) + 1

        return res
