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
            elif len(brackets) > 0:
                if brackets.pop() != c:
                    return False
            else:
                return False

        if len(brackets) > 0:
            return False

        return True