class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # The stack will store the current combination being generated
        stack = []
        # The result will store all valid combinations found
        result = []

        # The backtrack function is where the recursive exploration happens
        def backtrack(opened, closed):
            # Base Case: If we've added `n` opening and `n` closing parentheses,
            # we have a valid combination, so we add it to the result.
            if opened == closed == n:
                result.append(''.join(stack))
                return
            
            # Decision 1: Add an opening parenthesis, if we haven't reached the limit
            if opened < n:
                stack.append('(')  # Make the decision
                backtrack(opened + 1, closed)  # Recursively explore the next state
                stack.pop()  # Undo the decision (backtrack)

            # Decision 2: Add a closing parenthesis, but only if it won't exceed the number of openings
            if closed < opened:
                stack.append(')')  # Make the decision
                backtrack(opened, closed + 1)  # Recursively explore the next state
                stack.pop()  # Undo the decision (backtrack)

        # Initial call to backtrack with 0 opened and 0 closed parentheses
        backtrack(0, 0)

        return result
