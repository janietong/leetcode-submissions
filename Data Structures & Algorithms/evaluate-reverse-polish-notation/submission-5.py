class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {'+', '*', '-', '/'}
        for char in tokens:
            if char == '+':
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(a + b)
            elif char == '-':
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(a - b)
            elif char == '*':
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(a * b)
            elif char == '/':
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(int(a / b))
            else:
                stack.append(int(char))
        return stack[0]
                