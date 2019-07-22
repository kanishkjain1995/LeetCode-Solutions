class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == '+':
                a = stack.pop()
                b = stack.pop()
                stack.append(a+b)
            elif token == '-':
                a = stack.pop()
                b = stack.pop()
                stack.append(b-a)
            elif token == '/':
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b/a))
            elif token == '*':
                a = stack.pop()
                b = stack.pop()
                stack.append(a*b)
            else:
                stack.append(int(token))
            # print(stack)
        return stack[0]
