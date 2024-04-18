class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:


        l= 0
        r= len(nums)-1

        while(l<=r):
            m= (l+r)//2
            if( nums[m]== target):
                s,e=m,m
                while(s!=0 and nums[s-1]==target):
                    s-=1
                while(e!=len(nums)-1 and nums[e+1]==target):
                    e+=1
                return [s,e]
            elif(nums[m]< target):
                l= m+1
            else:
                r= m-1
        return [-1,-1]

        