class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        n  =len(intervals)
        intervals.sort(key = lambda x: x[1])

        count = 0 


        s , e = intervals[0]

        i = 1
        while i < n:

            while i < n and intervals[i][0] < e:
                count += 1
                i += 1
            
            if i<n:
                e = intervals[i][1]
            i += 1
        

        return count