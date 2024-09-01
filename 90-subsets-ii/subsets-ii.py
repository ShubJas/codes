class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        

        result = []
        n = len(nums)

        nums.sort()

        def backtrack(i,stack):

            if i == n:
                result.append(stack[:])
                return
            


            stack.append(nums[i])
            backtrack(i+1,stack)

            stack.pop()
            i += 1
            while i <n and nums[i] == nums[i-1]:
                i+=1
            backtrack(i,stack)
        
        backtrack(0,[])

        return result