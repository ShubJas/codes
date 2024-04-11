class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # we want the string to be in increasing so that we can remove directly from right
        #  for decreasing order case pop if new element is less than the one in stack till k is non zero is still incresing and stack isnt empty
        
        # monotonic stack
        stack=[] 
        
        for n in num:
            while k > 0 and stack and stack[-1] > n:
                k -= 1
                stack.pop()
            if stack or n != '0':  # Prevents leading zeros
                stack.append(n)
        
        # Remove the remaining k digits from the end if k is still > 0
        stack = stack[:-k] if k else stack
        
        # Convert stack back to string
        res = "".join(stack)
        
        return res if res else "0"

        