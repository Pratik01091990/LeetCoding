
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in tokens:
            if i.isnumeric() or (i[0] == '-' and i[1:].isnumeric()):
                stack.append(int(i))
            else:
                b = stack.pop()
                a = stack.pop()

                if i == '+':
                    stack.append(a + b)
                elif i == '-':
                    stack.append(a - b)
                elif i == '*':
                    stack.append(a * b)
                elif i == '/':
                    stack.append(int(a / b))

        return stack[0]
