class Solution:
    def getSum(self, a: int, b: int) -> int:

        # Helper function to perform the addition using bitwise operations
        def sum(a, b):
            # Base case: if one of the numbers is zero, return the other
            # This is because adding zero to any number does not change its value
            if not a or not b:
                return a or b
            
            # Recursive case:
            # - XOR (^) adds the bits of a and b where there is no carry.
            # - AND (&) finds the carry bits, and shifting them left by 1 (<< 1)
            #   prepares them to be added in the next significant bit position.
            return sum(a ^ b, (a & b) << 1)
        
        # Check if a and b have opposite signs
        if a * b < 0:
            # If a is positive and b is negative, swap them to simplify the logic
            if a > 0:
                return self.getSum(b, a)
            
            # If b is the two's complement of a, the result is zero
            # This means that a + b = 0 because they are exact opposites
            if sum(~a, 1) == b:
                return 0

            # If -a < b, the sum will be positive. We handle this by computing -add(-a, -b)
            # where ~a + 1 and ~b + 1 give the negative values of a and b, respectively.
            # The result is then negated to obtain the correct positive sum.
            # Emulating Subtraction
            if sum(~a, 1) < b:
                return sum(~sum(sum(~a, 1), sum(~b, 1)), 1)
        
        # If a and b have the same sign, or if -a > b > 0, directly compute the sum
        #  a positive number being added to a magnitude larger negative number
        return sum(a, b)


    
'''
-a < b Case: The function handles this by negating the sum of the two negative counterparts, ensuring the result is positive.
(-a) > b > 0 Case: The function directly adds the numbers, resulting in the correct negative sum when the magnitude of a exceeds that of b
'''



# class Solution:
#     def getSum(self, a: int, b: int) -> int:


#         while b:
#             carry = (a & b) << 1
#             a = a ^ b
#             b = carry
        

#         return a