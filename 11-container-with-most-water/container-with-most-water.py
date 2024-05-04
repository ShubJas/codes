class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxarea=0
        
        l = 0
        r = len(height) - 1

        while(l<r):
            area = (r-l) * min(height[l],height[r]) 
            maxarea = max(maxarea,area)

            if height[l] < height[r]:
                l+=1
            
            else:
                r-=1
        return maxarea

        # maxarea = 0

        # for l in range(len(height)-1):
        #     for r in range(l,len(height)):
        #         area = (r - l) * min(height[l],height[r])
            
        #         maxarea = max(maxarea,area)
        # return maxarea
        