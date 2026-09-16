class Solution:
    def isValid(self, s: str) -> bool:
        brackets = []

        for c in s:
            if c == '(':
                brackets.append(')')
            elif c == '[':
                brackets.append(']')
            elif c == '{':
                brackets.append('}')
            elif not brackets or brackets.pop() != c:
                return False

        return not brackets