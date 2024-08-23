class Solution:
    def evalRPN(self, tokens: List[str]) -> int:


        stack = []
        op = ['*','+','-','/']
        op = set(op)

        for x in tokens:

            if x not in op:
                stack.append(x)
            
            else:
                n1 = int(stack.pop())
                n2 = int(stack.pop())
                print()
                print(n2)
                print(x)
                print(n1)

                print()

                ans = 0
                if x == '*':
                    ans = n2 * n1
                elif x == '/':
                    if n1 < 0 and n2<0:
                        ans = abs(n2) // abs(n1)
                    elif n1 < 0 or n2 < 0:
                        ans = abs(n2) // abs(n1)
                        ans = -ans
                    else:
                        ans = n2 // n1
                elif x == '+':
                    ans = n2 + n1
                else:
                    ans = n2 - n1
                
                stack.append(str(ans))
        
        return int(stack.pop())
        