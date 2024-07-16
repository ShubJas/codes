class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        if n==1:
            return n

        inco = [0] * (n+1)
        outgo = [0] * (n+1)
        for x in trust:
            inco[x[1]] +=1
            outgo[x[0]] +=1
        for j,val in enumerate(inco):
            if val == n-1 and outgo[j] == 0:
                return j

        return -1