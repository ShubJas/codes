class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
                
        l = 0
        r = len(numbers)-1

        while(l<r):

            if numbers[l]+ numbers[r] < target:
                l = l+1
                

            elif numbers[l]+ numbers[r] > target:
                r = r-1
            else:
                return [l+1,r+1]


        # for l in range(len(numbers) - 1):
        #     r = l + 1
        #     while r < len(numbers):
        #         total = numbers[l] + numbers[r]
        #         if total == target:
        #             return [l + 1, r + 1]
        #         elif total > target:
        #             # If the total is greater than the target, no need to check further to the right
        #             break
        #         r += 1



        
        