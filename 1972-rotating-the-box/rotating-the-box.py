class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        rows = len(box)
        cols = len(box[0])
        
        # Apply gravity using two pointers
        for r in range(rows):
            write = cols - 1  # Start the write pointer at the end of the row
            for read in reversed(range(cols)):  # Read from right to left
                if box[r][read] == '*':
                    write = read - 1  # Reset write position at the left of the obstacle
                elif box[r][read] == '#':
                    box[r][write] = '#'  # Move stone to the new position
                    if write != read:
                        box[r][read] = '.'  # Clear the original stone position
                    write -= 1  # Move the write pointer to the next available spot

        # Rotate the box to result (90 degrees clockwise)
        result = [['' for _ in range(rows)] for _ in range(cols)]
        for r in range(rows):
            for c in range(cols):
                result[c][rows - r - 1] = box[r][c]

        return result
