class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        

        stack = []
        result = []

        def backtrack(no, nc):


            if no == nc == n:
                result.append(''.join(stack))
                return
            
            if no < n:
                stack.append('(')
                backtrack(no+1,nc)
                stack.pop()

            if nc < no:
                stack.append(')')
                backtrack(no,nc+1)
                stack.pop()
        

        backtrack(0,0)
        return result