class Solution:
    def trap(self, height: List[int]) -> int:
        
        l = 0
        r = len(height)-1
        lmax = height[l]
        rmax = height[r]
        total =0

        while(l<r):
            if lmax>rmax:
                r-=1
                rmax = max(rmax,height[r])
                total+= rmax - height[r]
            else:
                l+=1
                lmax = max(lmax,height[l])
                total+= lmax - height[l]
        
        return total













        # total = 0

        # for i in range(1,len(height)-1):

        #     curr = min(max(height[:i]),max(height[i+1:])) - height[i] 
        #     curr = curr if curr > 0 else 0
        #     # print(curr)

        #     total+=curr

        #     # print(total)
        # return total

        
        