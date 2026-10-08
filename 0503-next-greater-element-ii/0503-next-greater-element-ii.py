class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        st = []
        res = [-1] * len(nums)

        for i, num in enumerate(nums):
            while st and num > nums[st[-1]]:
                res[st.pop()] = num
            
            st.append(i)

        for i, num in enumerate(nums):
            while st and num > nums[st[-1]]:
                res[st.pop()] = num

        return res
