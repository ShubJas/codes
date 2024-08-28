class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        count = defaultdict(int)


        for task in tasks:
            count[task] += 1

        tasks = [-cnt for cnt in count.values()]
        heapq.heapify(tasks)
        q = deque()
        time = 0
        while tasks or q:

            time +=1

            if tasks: 
                cnt = heapq.heappop(tasks) + 1
                if cnt:
                    q.append((cnt,time+n))
            
            if q and q[0][1] == time:
                heapq.heappush(tasks,q.popleft()[0])

        return time