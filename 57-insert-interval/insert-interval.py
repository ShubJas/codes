class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        ns,ne = newInterval 
        result = []
        i = 0

        while i < n and intervals[i][1] < ns:
            result.append(intervals[i])
            i+=1
        

        while i< n and intervals[i][0] <= ne:
            ns = min(ns,intervals[i][0])
            ne = max(ne,intervals[i][1])
            i+=1


        result.append([ns,ne])

        while i<n:
            result.append(intervals[i])
            i+=1

        return result 
