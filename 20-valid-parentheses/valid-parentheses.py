class Solution:
    def isValid(self, s: str) -> bool:


        mapper = {']':'[','}':'{',')':'('}
        stack = []
        for c in s:
            if c not in mapper:
                stack.append(c)
            else:
                if not stack or stack[-1] != mapper[c]:
                    return False
                stack.pop()
        
        return not stack
                
        