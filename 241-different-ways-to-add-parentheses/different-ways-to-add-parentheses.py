class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        
        result = []

        n = len(expression)
        for i in range(n):
            ch = expression[i]
            
            if ch in '+-*':
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i+1:])
            
                for n1 in left:
                    for n2 in right:
                        if ch == '+':
                            result.append(n1 + n2)
                        elif ch == '-':
                            result.append(n1 - n2)
                        else:
                            result.append(n1 * n2)

        # If no operators were found, it means the expression is just a number.
        if not result:
            return [int(expression)]  # Directly return a list containing the integer

        return result
