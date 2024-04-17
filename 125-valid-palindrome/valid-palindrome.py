class Solution:
    def alnum(self, c):
        # Correcting the usage of string literals for character ASCII comparisons
        return ((ord('a') <= ord(c) <= ord('z')) or 
                (ord('A') <= ord(c) <= ord('Z')) or 
                (ord('0') <= ord(c) <= ord('9')))
        
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        
        while l < r:
            # Fixed missing self reference to alnum
            while l < r and not self.alnum(s[l]):
                l += 1
            while l < r and not self.alnum(s[l]):
                l += 1
            while l < r and not self.alnum(s[r]):
                r -= 1
                
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
            
        return True

        
        
        
        # # Using methods
        # string= ""
        # for c in s:
        #     if c.isalnum():
        #         string+= c.lower()
        # return string == string[::-1]

        