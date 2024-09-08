class Solution:
    def myPow(self, x: float, n: int) -> float:


        

        def calc(x,n):

            if n == 0:
                return 1

            if n % 2 == 0:
                return calc(x * x, n // 2)
            else:
                return x * calc(x, n - 1)


        ans = calc(x,abs(n))
        if n >= 0:
            return ans
        else:
            return 1/ans




# class Solution:
#     def myPow(self, x: float, n: int) -> float:
        
        
#         p = 1
#         for _ in range(abs(n)):
#             p*=x

#         if n >=0:
#             return p
#         else:
#             return 1/p




# class Solution:
#     def myPow(self, x: float, n: int) -> float:
        
        
        
#         def calcpos(i):

#             if i == 0:
#                 return 1
            
#             return calcpos(i-1) * x
        

#         def calcneg(i):

#             if i == 0:
#                 return 1
            
#             return calcneg(i-1) / x
        

#         if n >=0:
#             return calcpos(n)
#         else:
#             return calcneg(abs(n))

