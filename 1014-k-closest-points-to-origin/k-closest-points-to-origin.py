class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        


        def dist(p1,points):
            return pow(p1[0],2)+pow(p1[1],2)
        

        pq = []
        for p in points:
            heapq.heappush(pq,(dist(p,points),p))
        
        result = []
        for _ in range(k):
            _, p = heapq.heappop(pq)
            result.append(p)
        return result