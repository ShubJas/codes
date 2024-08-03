class Solution:
    def maxProduct(self, nums: List[int]) -> int:


        # Best intuitive solution

        #  if all are +ve - mul all
        #  if count of (-1ves) is even - mul all
        #  if count of (-1ves) is odd - max(prefix,suffix) -   3 2 4  -1  3 7 6
        #                                                     pref mul   suffix mul
        #  if 0 comes in btwn then treat as seperate array(restart) - so reset pre,suf to 1


        n = len(nums)
        prefix_mul = suffix_mul = 1
        maxi = -float('inf') # global max
        for i in range(n):

            if prefix_mul == 0:
                prefix_mul = 1
            if suffix_mul == 0:
                suffix_mul = 1


            prefix_mul *= nums[i]
            suffix_mul *= nums[n-1-i]

            maxi = max(maxi,max(prefix_mul,suffix_mul))
        
        return maxi










        # curr_max = 1
        # maxi = 0

        # for curr in nums:
        #     curr_max = max(curr,curr_max*curr)
        #     maxi = max(maxi,curr_max)

        # return maxi if len(nums)>1 else nums[0]


        # # Brute better
        # n = len(nums)

        # maxi = -float('inf')
        # for i in range(n):
        #     prod = 1
        #     for j in range(i,n):
        #         prod *= nums[j]
        #         maxi = max(maxi,prod)
        
        # return maxi



        #  #Full brute
        # n = len(nums)

        # maxi = -float('inf')
        # for i in range(n):
        #     for j in range(i,n):
        #         prod = 1
        #         for k in range(i,j+1):
        #             prod *= nums[k]
        #         maxi = max(maxi,prod)
        
        # return maxi

