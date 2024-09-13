class Solution:
    def candy(self, ratings: List[int]) -> int:
        


        left = [1]
        right = [1]
        n = len(ratings)

        for i in range(n-1):

            if ratings[i+1] > ratings[i]:
                left.append(left[-1] + 1)
            else:
                left.append(1)
            
            if ratings[n-i-2] > ratings[n-i-1]:
                right.append(right[-1] + 1)
            else:
                right.append(1)
        


        
        right = right[::-1]


        # print([max(l,r) for l,r in zip(left,right)])
        return sum([max(l,r) for l,r in zip(left,right)])
