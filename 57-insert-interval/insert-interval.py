class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        merged = []
        i = 0
        n = len(intervals)
        
        ns, ne = newInterval
        
        # Add all intervals before the new interval (non-overlapping)
        while i < n and intervals[i][1] < ns:
            merged.append(intervals[i])
            i += 1
        
        # Merge overlapping intervals with the new interval
        while i < n and intervals[i][0] <= ne:
            ns = min(ns, intervals[i][0])
            ne = max(ne, intervals[i][1])
            i += 1
        
        # Add the merged interval
        merged.append([ns, ne])
        
        # Add all intervals after the new interval (non-overlapping)
        while i < n:
            merged.append(intervals[i])
            i += 1
        
        return merged
