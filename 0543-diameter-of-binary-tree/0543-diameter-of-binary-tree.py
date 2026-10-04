# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        st = [(root, False)]
        heights = {None: 0}
        diameter = 0

        while st:
            node, visited = st.pop()

            if node is None:
                continue

            if not visited:
                st.append((node, True))
                st.append((node.right, False))
                st.append((node.left, False))
            else:
                left = heights[node.left]
                right = heights[node.right]

                diameter = max(diameter, left + right)
                heights[node] = 1 + max(left, right)

        return diameter