# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        st = []
        res = []
        curr = root

        while curr or st:
            while curr:
                st.append(curr)
                curr = curr.left

            curr = st.pop()
            res.append(curr.val)

            curr = curr.right

        return res[k - 1]
                    