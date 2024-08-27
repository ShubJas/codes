# Greedy arrangement - count no. of idels + tasks
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        count = defaultdict(int)

        for task in tasks:
            count[task] +=1
        
        total_tasks = len(tasks)


        max_count = max(count.values())
        
        no_of_max = list(count.values()).count(max_count)

        divisions = max_count - 1
        division_length = n - (no_of_max-1)
        empty_slots = divisions * division_length
        available_tasks = total_tasks - max_count * no_of_max  
        
        idles = max(0,empty_slots-available_tasks)


        return total_tasks + idles

