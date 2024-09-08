class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        result = []
        n = len(s)
        def ispal(i,j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i+=1
                j-=1
            
            return True

        def backtrack(i,stack):

            if i == n:
                result.append(stack[:])
                return
            

            for j in range(i,n):
                if ispal(i,j):
                    stack.append(s[i:j+1])
                    backtrack(j+1,stack)
                    stack.pop()
                    # backtrack(i+1,stack)
            

        backtrack(0,[])

        return result


