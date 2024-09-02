class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        
        n = len(chalk)
        
        S = sum(chalk)
        k = k % S

        i = 0
        while k >= chalk[i]:
            k -= chalk[i]
            # print(f"k - {k} student - {i}")
            i+=1
            i = i % n

            
        
        return i 



# class Solution:
#     def chalkReplacer(self, chalk: List[int], k: int) -> int:
        
#         n = len(chalk)
#         i = 0
#         while k >= chalk[i]:
#             k -= chalk[i]
#             # print(f"k - {k} student - {i}")
#             i+=1
#             i = i % n

        
#         return i 