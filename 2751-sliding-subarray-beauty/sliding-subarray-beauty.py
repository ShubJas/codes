from sortedcontainers import SortedList

class Solution:
    def getSubarrayBeauty(self, nums, k, x):
        result = []
        sl = SortedList()  # This will only hold negative numbers
        
        # Initial population of the sorted list with the first subarray
        for i in range(k):
            if nums[i] < 0:
                sl.add(nums[i])

        # Calculate beauty for the first subarray
        if len(sl) >= x:
            result.append(sl[x-1])  # Access x-1 because of 0-based indexing in Python
        else:
            result.append(0)

        # Slide the window across the array
        for i in range(k, len(nums)):
            if nums[i-k] < 0:
                sl.remove(nums[i-k])  # Remove the element that is sliding out of the window
            if nums[i] < 0:
                sl.add(nums[i])  # Add the new element that is sliding into the window

            # Calculate beauty for the current subarray
            if len(sl) >= x:
                result.append(sl[x-1])
            else:
                result.append(0)

        return result
