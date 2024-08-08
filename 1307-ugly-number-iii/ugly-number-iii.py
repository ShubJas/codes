# least common multiples (LCM) and the inclusion-exclusion principle
class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:

        def lcm(x, y):
            return x * y // math.gcd(x, y)
        

        def feasible(num) -> bool:
            count = num // a + num // b + num // c  # count of each psble a,b,c
            count -= num // lcm_ab + num // lcm_ac + num // lcm_bc   # remove overcountsn of each psble a,b,c
            count += num // lcm_abc # add the count removed of all of them
            return count >= n
        
        lcm_ab = lcm(a, b)
        lcm_bc = lcm(b, c)
        lcm_ac = lcm(a, c)
        lcm_abc = lcm(lcm_ab, c)

        l = 1
        r= n * min(a,b,c)
        
        while l<r:
            m = (l+r)//2

            if feasible(m):
                r = m
            else:
                l = m+1
        return l
        