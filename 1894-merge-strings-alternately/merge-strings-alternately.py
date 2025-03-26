class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        newword = ""
        n1 = len(word1)
        n2 = len(word2)
        n = min(n1,n2)

        for i in range(n):

            newword += word1[i]
            newword += word2[i]
        
        if n1 > n:
            newword+= word1[n:]
        
        if n2 > n:
            newword+= word2[n:]
        

        return newword