# Greedy approach
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Step 1: Count the frequency of each task
        # Using defaultdict to store the frequency of each task
        count = defaultdict(int)
        
        # Iterate over each task and increment its count in the dictionary
        for task in tasks:
            count[task] += 1
        
        # Total number of tasks in the input list
        total_tasks = len(tasks)

        # Step 2: Determine the maximum frequency of any single task
        # Find the task that appears the most times
        max_count = max(count.values())
        
        # Step 3: Count how many tasks have this maximum frequency
        # There could be more than one task that appears with the maximum frequency
        no_of_max = list(count.values()).count(max_count)

        # Step 4: Calculate the number of parts or "divisions" needed between the most frequent tasks
        # Since we have max_count occurrences of the most frequent task, we have (max_count - 1) divisions between them
        divisions = max_count - 1
        
        # Step 5: Calculate the length of each division (number of idle slots needed between the most frequent tasks)
        # The length of each division is the cooldown period 'n', minus the space occupied by other tasks that have the same frequency
        # This is because if there are other tasks with the same frequency, they can be placed in those idle slots
        division_length = n - (no_of_max - 1)
        
        # Step 6: Calculate the total number of empty slots that need to be filled
        # This is the number of divisions multiplied by the length of each division
        # This represents the minimum number of idle slots required to place the most frequent tasks
        empty_slots = divisions * division_length
        
        # Step 7: Calculate the number of remaining tasks after accounting for the most frequent ones
        # These remaining tasks are available to fill in the empty slots
        available_tasks = total_tasks - (max_count * no_of_max)
        
        # Step 8: Calculate the number of idle slots that remain after placing the available tasks
        # If available_tasks are not enough to fill the empty_slots, the remaining slots are idle
        # If available_tasks are enough or more, idles will be zero since all slots are filled
        idles = max(0, empty_slots - available_tasks)

        # Step 9: The minimum time required to complete all tasks is the sum of all tasks and the idles
        # If there are no idle slots, the total time is just the number of tasks
        # If there are idle slots, the total time is the number of tasks plus the idle slots
        return total_tasks + idles
