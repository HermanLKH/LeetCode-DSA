"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []

        st = [root]
        res = []
        
        while st:
            node = st.pop()
            res.append(node.val)

            if node.children:
                for c in node.children[::-1]:
                    st.append(c)
        
        return res