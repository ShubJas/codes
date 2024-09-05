class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
         
        m = len(rolls)
        S = mean * (n + m) - sum(rolls) 

        if S / n > 6 or S / n < 1:
            return []


        result = []
        ele  =S // n
        rem = S % n
        for _ in range(n):
            result.append(S // n)
        

        for i in range(rem):
            result[i] += 1
        
        return result