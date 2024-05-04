class Solution:
    def fourSum(self, nums, target):
        
        nums.sort()
        result = []
        for l in range(len(nums)-3):


            if l>0 and nums[l] == nums[l-1]:
                continue
            

            for m1 in range(l+1,len(nums)-2):

                if m1> l+ 1 and nums[m1] == nums[m1-1]:
                    continue
                


                m2 = m1+1
                r = len(nums)-1

                while m2 < r:

                    total = nums[l] + nums[m1] + nums[m2] + nums[r]

                    if total==target:

                        result.append([nums[l],nums[m1],nums[m2],nums[r]])

                        m2+=1
                        r-=1

                        while m2<r and nums[m2] == nums[m2-1]:
                            m2+=1
                        
                        while m2<r and nums[r] == nums[r+1]:
                            r-=1
                        
                    elif total > target:
                        r-=1
                    
                    else:
                        m2+=1
        
        return result
                            
        
        
        
        
        
        
        
        
        
        
        
        # def findNsum(l, r, target, N, result, results):
        #     if r-l+1 < N or N < 2 or target < nums[l]*N or target > nums[r]*N:  
        #         return
        #     if N == 2: 
        #         while l < r:
        #             s = nums[l] + nums[r]
        #             if s == target:
        #                 results.append(result + [nums[l], nums[r]])
        #                 l += 1
        #                 while l < r and nums[l] == nums[l-1]:
        #                     l += 1
        #             elif s < target:
        #                 l += 1
        #             else:
        #                 r -= 1
        #     else:
        #         for i in range(l, r+1):
        #             if i == l or (i > l and nums[i-1] != nums[i]):
        #                 findNsum(i+1, r, target-nums[i], N-1, result+[nums[i]], results)

        # nums.sort()
        # results = []
        # findNsum(0, len(nums)-1, target, 4, [], results)
        # return results