class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Initialize a variable `x` to 0.
        # This variable will be used to store the result of XOR operations.
        # Why start with 0? Because XOR-ing any number with 0 returns the number itself, making 0 a neutral starting value.
        x = 0

        # Iterate over each number `n` in the list `nums`.
        # The idea is to XOR all the numbers together.
        for n in nums:
            # XOR the current value of `x` with `n` and store the result back in `x`.
            # How it works: XOR of two identical numbers is 0 (a ^ a = 0),
            # and XOR of any number with 0 is the number itself (a ^ 0 = a).
            # Therefore, pairs of identical numbers in the list will cancel each other out, 
            # leaving only the single number that doesn't have a pair.
            x ^= n
        
        # After the loop, `x` contains the number that appears only once in the list.
        # This is because all other numbers have been canceled out through the XOR operation.
        return x
