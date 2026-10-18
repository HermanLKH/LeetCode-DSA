# Time complexity:  O(N)
# Space complexity: O(N)
class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        odd_cnt, res = 0, 0
        lookup = {0: 1}

        for num in nums:
            odd_cnt += num % 2
            
            res += lookup.get(odd_cnt - k, 0)

            lookup[odd_cnt] = lookup.get(odd_cnt, 0) + 1

        return res
