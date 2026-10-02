"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []

        res = []

        q = deque()
        q.append(root)

        while q:
            size = len(q)
            level = []

            for _ in range(size):
                node = q.popleft()
                level.append(node.val)

                if node.children:
                    for c in node.children:
                        q.append(c)

            res.append(level)
            
        return res