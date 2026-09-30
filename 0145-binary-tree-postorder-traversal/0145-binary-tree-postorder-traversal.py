# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode | None) -> list[int]:
        if root is None:
            return []

        res = []
        st = [root]
        visited = {}
        curr = root

        while curr or st:
            while curr:
                if curr.left and not visited.get(curr.left):
                    curr = curr.left
                    st.append(curr)
                elif curr.right and not visited.get(curr.right):
                    curr = curr.right
                    st.append(curr)
                else:
                    curr = None
                
            node = st.pop()
            visited[node] = True
            res.append(node.val)
            curr = st[-1] if st else None

        return res