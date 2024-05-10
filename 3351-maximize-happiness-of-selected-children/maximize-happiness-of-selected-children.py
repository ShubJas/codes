class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:

        
        total = 0
        happiness.sort(reverse=True)
        for i in range(k):
            curr = happiness[i] - i
            total += curr if curr > 0 else 0

        return total
        
        
        
        
        # total = 0
        # hashset = defaultdict(list)
        # for i in range(len(happiness)):
        #     hashset[happiness[i]].append(i)
        # happiness.sort()
        # for i in range(k):
        #     curr =happiness[len(happiness)-1-i]
        #     total += curr - i if curr - i > 0 else 0
        #     del hashset[curr][0]
        
        # return total
        