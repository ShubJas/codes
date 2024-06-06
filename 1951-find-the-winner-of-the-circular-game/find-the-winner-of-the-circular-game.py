class Solution:
    def findTheWinner(self, n: int, k: int) -> int:

        friends = [ i for i in range(1,n+1)]
        index = 0
        while friends:
            index = (index + k-1) % len(friends)
            win = friends.pop(index)
        
        return win




        # q = deque([ i+1 for i in range(n)])

        # while len(q) > 1:

        #     t = k -1
        #     while t:
        #         q.append(q.popleft())
        #         t-=1
            
        #     q.popleft()
        
        # return q[0]

        