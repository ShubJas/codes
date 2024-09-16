class Solution:
    def findMinDifference(self, A):
        def convert(time):
            return int(time[:2]) * 60 + int(time[3:])
        
        # Convert the times to minutes and sort them
        minutes = sorted(map(convert, A))
        
        # Find the minimum difference
        min_diff = float('inf')
        for i in range(1, len(minutes)):
            min_diff = min(min_diff, minutes[i] - minutes[i - 1])
        
        # Check the difference between the last and first, considering the 24-hour wrap around
        min_diff = min(min_diff, 24 * 60 - (minutes[-1] - minutes[0]))
        
        return min_diff
