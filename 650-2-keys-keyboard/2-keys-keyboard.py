class Solution:
    def minSteps(self, n: int) -> int:


        
        def calc(l,clipboard):

            if l == n:
                return 0
            
            if l>n:
                return float('inf')

            copy = paste = float('inf')
            if l!= clipboard:
                copy = 1 + calc(l,l)
            
            if clipboard>0:
                paste = 1 + calc(l + clipboard,clipboard)
            
            return min(copy,paste)
        

        
        return calc(1,0)