class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])

        st = []
        operators = ('+', '-', '*', '/')

        for i, token in enumerate(tokens):
            if token in operators:
                num1, j = st.pop()
                num2, k = st.pop()

                if j < k:
                    temp = num2
                    num2 = num1
                    num1 = temp

                if token == '+':
                    num2 += num1
                elif token == '*':
                    num2 *= num1
                elif token == '-':
                    num2 -= num1
                else:
                    num2 = int(num2 / num1)

                st.append((num2, max(j, k)))
            else:
                st.append((int(token), i))
        
        return st[0][0]
