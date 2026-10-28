class Solution:
    def answerQueries(self, nums: list[int], queries: list[int]) -> list[int]:
        nums = sorted(nums)
        res = []
        
        for q in queries:
            curr = q
            cnt = 0

            for num in nums:
                if curr - num >= 0:
                    curr -= num
                    cnt += 1
            
            res.append(cnt)

        return res
                    