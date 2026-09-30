# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        st = []
        res = []
        curr = root

        while curr or st:
            while curr:
                st.append(curr)
                curr = curr.left

            node = st.pop()
            res.append(node.val)

            curr = node.right

        return res