class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        # Special case: if either number is "0", the product is "0".
        if '0' in [num1, num2]:
            return '0'

        # Get the lengths of the two numbers.
        n1 = len(num1)
        n2 = len(num2)

        # Reverse both strings to facilitate easier multiplication (from right to left, like manual multiplication).
        # This is because multiplication proceeds from the least significant digit to the most significant.
        num1, num2 = num1[::-1], num2[::-1]

        # Initialize a result list to hold the intermediate results.
        # The size of the result list is `n1 + n2` because the maximum possible number of digits in the result of
        # multiplication of two numbers is the sum of their individual lengths.
        result = [0] * (n1 + n2)

        # Nested loops to simulate multiplication digit by digit (similar to the long multiplication algorithm).
        for i1 in range(n1):
            for i2 in range(n2):
                
                # Multiply the current digits from num1 and num2.
                # Convert the character digits to integers using `int()`.
                result[i1 + i2] += int(num1[i1]) * int(num2[i2])
                
                # If there's a carry, add it to the next position.
                # For example, if result[i1 + i2] = 15, then 5 remains at result[i1 + i2] and 1 (carry) is added
                # to result[i1 + i2 + 1].
                result[i1 + i2 + 1] += result[i1 + i2] // 10  # Carry forward the tens digit.
                
                # Retain only the last digit at the current position (this handles the ones place for the current product).
                result[i1 + i2] %= 10  # Only the last digit stays at result[i1 + i2].

        # At this point, result contains the multiplication result in reverse order (each element is a digit).

        # Reverse the result list to get the correct order of the final product.
        result = result[::-1]

        # Find the first non-zero digit (skip any leading zeros that might have been generated).
        # This is because the result might have extra leading zeros, and we want to strip them out.
        start = 0
        while result[start] == 0:
            start += 1

        # Convert the result list (digits) to a string by mapping each digit to a string and joining them together.
        result = map(str, result[start:])
        
        # Return the final product as a string.
        return ''.join(result)





# class Solution:
#     def multiply(self, num1: str, num2: str) -> str:
        
#         return str(int(num1)*int(num2))