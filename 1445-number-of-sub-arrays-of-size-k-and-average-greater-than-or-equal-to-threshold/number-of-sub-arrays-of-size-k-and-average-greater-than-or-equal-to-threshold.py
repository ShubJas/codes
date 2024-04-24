class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0 
        winsum = sum(arr[:k])
        if winsum/k >= threshold:
            count+=1
        
        for i in range(k, len(arr)):
            winsum = winsum + arr[i] - arr[i-k]
            if winsum/k >= threshold:
                count+=1
        return count


        