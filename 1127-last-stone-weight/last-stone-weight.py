class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        if not stones:
            return 0
        stones = [-x for x in stones]
        heapq.heapify(stones)

        print(stones)

        while len(stones) > 1:

            heaviest = heapq.heappop(stones)
            second_heaviest = heapq.heappop(stones)

            if heaviest != second_heaviest:
                heapq.heappush(stones,heaviest-second_heaviest)
        
        return -stones[0] if stones else 0
