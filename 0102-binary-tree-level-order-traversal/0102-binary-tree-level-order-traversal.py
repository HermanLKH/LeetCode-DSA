# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return []

        q = deque()
        q.append(root)
        res = []

        while q:
            level = []
            size = len(q)

            for _ in range(size):
                n = q.popleft()
                level.append(n.val)

                if n.left:
                    q.append(n.left)

                if n.right:
                    q.append(n.right)

            res.append(level)
            level = []

        return res