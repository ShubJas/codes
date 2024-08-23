class Solution:
    def evalRPN(self, tokens: List[str]) -> int:


        stack = []
        for token in tokens:
            if token == '+':
                b = stack.pop()
                a = stack.pop()
                stack.append(int(a) + int(b))
            elif token == '-':
                b = stack.pop()
                a = stack.pop()
                stack.append(int(a) - int(b))
            elif token == '*':
                b = stack.pop()
                a = stack.pop()
                stack.append(int(a) * int(b))
            elif token == '/':
                b = stack.pop()
                a = stack.pop()
                stack.append(int(int(a) / int(b)))
            else:
                stack.append(token)

            # print(stack)
        return int(stack[0])
        