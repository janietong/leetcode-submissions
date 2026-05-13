class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {'+', '*', '-', '/'}
        for char in tokens:
            if char in ops:
                b = int(stack.pop())
                a = int(stack.pop())

                if char == '+':
                    stack.append(a + b)
                elif char == '-':
                    stack.append(a - b)
                elif char == '*':
                    stack.append(a * b)
                else:
                    stack.append(int(a / b))
            else:
                stack.append(int(char))
        return stack[0]
                