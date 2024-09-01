from typing import List

class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        # Check if the total number of elements matches m * n
        if len(original) != m * n:
            return []

        # Initialize the result array
        result = [[-1] * n for _ in range(m)]

        # Fill the result array
        for i in range(len(original)):
            col = i % n
            row = i // n
            result[row][col] = original[i]

        return result
