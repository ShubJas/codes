class Solution:
    def parseBoolExpr(self, expression: str) -> bool:

        def parse(exp):
            if exp[0] == '&':
                # Extract the content inside the parentheses
                exp = exp[2:-1]
                # Evaluate each sub-expression and return 'f' if any is 'f'
                sub_expressions = split_expressions(exp)
                for sub_expr in sub_expressions:
                    if parse(sub_expr) == 'f':
                        return 'f'
                return 't'
            
            elif exp[0] == '|':
                # Extract the content inside the parentheses
                exp = exp[2:-1]
                # Evaluate each sub-expression and return 't' if any is 't'
                sub_expressions = split_expressions(exp)
                for sub_expr in sub_expressions:
                    if parse(sub_expr) == 't':
                        return 't'
                return 'f'
            
            elif exp[0] == '!':
                # Extract the content inside the parentheses
                exp = exp[2:-1]
                # Evaluate the sub-expression and negate its result
                sub_expressions = split_expressions(exp)
                assert len(sub_expressions) == 1, "NOT operation should have exactly one operand"
                return 'f' if parse(sub_expressions[0]) == 't' else 't'
            
            # Return the value for 't' or 'f'
            return exp

        def split_expressions(exp):
            # Helper function to split the sub-expressions inside parentheses
            sub_expressions = []
            start = 0
            depth = 0
            for i, char in enumerate(exp):
                if char == '(':
                    depth += 1
                elif char == ')':
                    depth -= 1
                elif char == ',' and depth == 0:
                    sub_expressions.append(exp[start:i])
                    start = i + 1
            # Add the last sub-expression
            sub_expressions.append(exp[start:])
            return sub_expressions

        # Parse the expression from the start
        return True if parse(expression) == 't' else False
