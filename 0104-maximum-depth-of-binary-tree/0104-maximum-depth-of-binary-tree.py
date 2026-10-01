# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        if not root:
            return 0
        
        q = deque([root])
        max_depth = 0

        while q:
            for _ in range(len(q)):
                n = q.popleft()

                if n.left:
                    q.append(n.left)

                if n.right:
                    q.append(n.right)

            max_depth += 1

        return max_depth