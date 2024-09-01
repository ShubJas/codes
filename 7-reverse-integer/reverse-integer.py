import math

class Solution:
    def reverse(self, x: int) -> int:
        # Define the minimum and maximum values for a 32-bit signed integer.
        MIN = -2147483648  # -2^31, the minimum possible value for a 32-bit signed integer
        MAX = 2147483647   #  2^31 - 1, the maximum possible value for a 32-bit signed integer

        # Initialize the result variable that will store the reversed number.
        res = 0
        
        # Loop until all digits of x are processed.
        while x:
            # Extract the last digit of x using fmod to handle negative numbers correctly.
            # math.fmod(x, 10) gives the remainder of x divided by 10, similar to x % 10,
            # but handles negative numbers in a more consistent way across Python versions.
            digit = int(math.fmod(x, 10))
            
            # Update x by removing the last digit. This is done by integer division.
            # In Python, x // 10 rounds towards negative infinity for negative numbers,
            # so we use int(x / 10) to get the floor division behavior.
            x = int(x / 10)
            
            # Check if appending the digit to res will cause an overflow.
            # If res is greater than MAX // 10, then adding any more digits would overflow.
            # If res is equal to MAX // 10, then we can only append digits <= MAX % 10 (which is 7) without overflowing.
            if res > MAX // 10 or (res == MAX // 10 and digit > MAX % 10):
                return 0  # Overflow detected, return 0.
            
            # Similarly, check for underflow for negative numbers.
            # If res is less than MIN // 10, then adding any more digits would underflow.
            # If res is equal to MIN // 10, then we can only append digits >= MIN % 10 (which is -8) without underflowing.
            if res < MIN // 10 or (res == MIN // 10 and digit < MIN % 10):
                return 0  # Underflow detected, return 0.
            
            # Append the digit to the reversed number by multiplying res by 10 and adding the digit.
            res = (res * 10) + digit

        # Return the final reversed number after all digits have been processed.
        return res

        


# class Solution:
#     def reverse(self, x: int) -> int:

#         rev = int(''.join([ch for ch in reversed(str(x) if x >= 0 else str(x)[1:])]))
        
#         if rev > 2**31 - 1 :
#             return 0

#         return rev if x >=0 else -rev  