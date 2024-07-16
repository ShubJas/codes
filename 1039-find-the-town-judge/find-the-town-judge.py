from collections import defaultdict
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if not trust and n == 1:
            return 1

        trust_count = [0] * (n + 1)
        trusted_by = [0] * (n + 1)

        for people, judge in trust:
            trust_count[people] += 1
            trusted_by[judge] += 1

        for i in range(1, n + 1):
            if trust_count[i] == 0 and trusted_by[i] == n - 1:
                return i

        return -1
        