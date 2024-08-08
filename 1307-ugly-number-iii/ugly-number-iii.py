class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:

        def lcm(x,y):

            return x*y // math.gcd(x,y)

        def feasible(num):
            count = num//a + num// b + num//c
            count-= num//lcm_ab + num//lcm_ac +num//lcm_bc
            count+= num//lcm_abc

            return count>=n

        
        lcm_ab = lcm(a,b)
        lcm_ac = lcm(a,c)
        lcm_bc = lcm(b,c)
        lcm_abc = lcm(lcm_ab,c)


        






        l = 1
        r = n * min(a,b,c)


        while l < r:

            mid = (l+r)//2
            if feasible(mid):
                r = mid
            else:
                l = mid + 1
        
        return l
        