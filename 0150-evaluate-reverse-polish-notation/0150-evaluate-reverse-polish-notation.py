class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        st = []
        operators = ('+', '-', '*', '/')

        for token in tokens:
            if token in operators:
                num1 = st.pop()
                num2 = st.pop()

                if token == '+':
                    num2 += num1
                elif token == '*':
                    num2 *= num1
                elif token == '-':
                    num2 -= num1
                else:
                    num2 = int(num2 / num1)

                st.append(num2)
            else:
                st.append(int(token))
        
        return st[0]
