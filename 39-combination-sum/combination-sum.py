class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        

        n = len(candidates)
        result = []


        def backtrack(S , i, stack):


            if S == target:
                result.append(stack[:])
                return

            
            if i == n or S > target:
                return 

            stack.append(candidates[i])
            backtrack(S + candidates[i], i , stack)
            stack.pop()
            backtrack(S, i + 1, stack)
        
        backtrack(0, 0, [])


        return result
