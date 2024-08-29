class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        # Initialize a stack to keep track of indices of the temperatures
        stack = []
        
        # Get the length of the temperatures list
        n = len(temperatures)
        
        # Initialize the result list with all zeros. This is because if no warmer day is found,
        # the result should be 0 for that day.
        result = [0] * n

        # Iterate over each temperature in the list using its index
        for i in range(n):
            
            # While the stack is not empty and the current temperature is higher
            # than the temperature at the index stored at the top of the stack
            while stack and temperatures[i] > temperatures[stack[-1]]:
                # Pop the index from the stack
                prev_index = stack.pop()
                
                # Calculate the difference in indices, which gives the number of days
                # we had to wait for a warmer temperature
                result[prev_index] = i - prev_index
            
            # Push the current index onto the stack
            # This means we are now waiting for a warmer day for the current day (index i)
            stack.append(i)

        # Return the result list which contains the number of days to wait for a warmer temperature
        return result
