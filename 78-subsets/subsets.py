class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)

        result = []

        def backtrack(i,stack):

            print(i)
            if i == n:
                result.append(stack[:])
                return
            
            stack.append(nums[i])
            backtrack(i+1,stack)
            stack.pop()
            backtrack(i+1,stack)


        backtrack(0,[])

        return result
            