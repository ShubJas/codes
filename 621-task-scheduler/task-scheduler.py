class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        count = defaultdict(int)


        for task in tasks:
            count[task] += 1

        max_count = max(count.values())
        no_of_max = list(count.values()).count(max_count)

        divisions = max_count - 1
        length_per_div = n - (no_of_max - 1)
        spaces = divisions * length_per_div
        a_tasks = len(tasks) - max_count * no_of_max
        idles = max(0,spaces - a_tasks)


        return len(tasks) + idles