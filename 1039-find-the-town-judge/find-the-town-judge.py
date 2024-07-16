class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        if n==1:
            return n

        inco = defaultdict(set)
        outgo = defaultdict(set)
        for x in trust:
            inco[x[1]].add(x[0])
            outgo[x[0]].add(x[1])
        for j,val in inco.items():
            if len(val) == n-1 and len(outgo[j]) == 0:
                return j

        return -1