class Solution:
    def findTheWinner(self, n: int, k: int) -> int:

        q = deque([ i+1 for i in range(n)])

        while len(q) > 1:

            t = k -1
            while t:
                q.append(q.popleft())
                t-=1
            
            q.popleft()
        
        return q[0]

        