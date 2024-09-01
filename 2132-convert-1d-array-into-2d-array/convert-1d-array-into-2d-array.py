from typing import List

class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        
        if len(original) != m * n:
            return []

        result = [[-1] * n for _ in range(m)]

        for i in range(len(original)):
            col = i % n
            row = i // n
            result[row][col] = original[i]

        return result
