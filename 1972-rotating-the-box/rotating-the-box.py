class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        rows = len(box)
        cols = len(box[0])
        
        # Move stones to the right
        for r in range(rows):
            boundary = cols  # Reset boundary to the end of each row initially
            for c in reversed(range(cols)):  # Start from the rightmost column
                if box[r][c] == '*':
                    boundary = c  # Reset boundary when hitting an obstacle
                elif box[r][c] == '#':
                    box[r][c] = '.'  # Clear the current stone position
                    boundary -= 1  # Move boundary left
                    box[r][boundary] = '#'  # Place the stone at the new boundary

        # Rotate the box to result
        result = [['' for _ in range(rows)] for _ in range(cols)]
        for r in range(rows):
            for c in range(cols):
                result[c][rows - r - 1] = box[r][c]

        return result
