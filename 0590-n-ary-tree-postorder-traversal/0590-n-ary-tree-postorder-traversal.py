"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []

        res = []
        st = [root]

        while st:
            node = st.pop()
            res.append(node.val)
            
            if node.children:
                for c in node.children:
                    st.append(c)

        return reversed(res)