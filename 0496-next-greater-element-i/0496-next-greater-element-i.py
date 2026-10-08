class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        st = []
        res = []
        records = dict.fromkeys(nums2, -1) 

        for i in range(len(nums2)):
            while st and nums2[i] > nums2[st[-1]]:
                records[nums2[st.pop()]] = nums2[i]
                
            st.append(i)

        for num in nums1:
            res.append(records[num])

        return res
