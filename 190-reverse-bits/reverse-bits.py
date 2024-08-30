class Solution:
    def reverseBits(self, n: int) -> int:
     
        # Initialize result to 0
        # This will hold the final reversed bits as we build it bit by bit.
        result = 0

        # Iterate over all 32 bits of the input integer 'n'
        for i in range(32):
            # Extract the i-th bit from 'n'
            # (n >> i) shifts the bits of 'n' to the right by 'i' positions.
            # & 1 isolates the least significant bit (the rightmost bit) after the shift.
            bit = (n >> i) & 1

            # Place the extracted bit in the reversed position in 'result'
            # 'bit << (31 - i)' shifts the bit to its new reversed position.
            result = result | (bit << (31 - i))
        
        # Return the final result, which now contains the bits of 'n' reversed.
        return result
