class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        
        allowed = set(list(allowed))

        count = 0

        for word in words:
            flag = True
            for ch in word:
                if ch not in allowed:
                    flag = False
                    break
            if flag:
                count+=1
        

        return count

# def countConsistentStrings(self, allowed: str, words: List[str]) -> int: 
#     alphabet = sum(1 << (ord(c) - ord('a')) for c in allowed)
#     return sum(all((alphabet & (1 << (ord(c) - ord('a'))) != 0) for c in word) for word in words)
