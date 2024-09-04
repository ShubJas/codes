class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Define the number of rows and columns
        rows = len(board)
        cols = len(board[0])
        
        # Define the DFS helper function
        def dfs(x, y, index):
            # If we've matched all characters in the word, return True
            if index == len(word):
                return True
            
            # If out of bounds, or the cell doesn't match the current word character, return False
            if x < 0 or x >= rows or y < 0 or y >= cols or board[x][y] != word[index]:
                return False
            
            # Temporarily mark the current cell as visited by changing its value
            temp = board[x][y]
            board[x][y] = "#"
            
            # Explore all four possible directions (down, right, up, left)
            found = (dfs(x + 1, y, index + 1) or
                     dfs(x, y + 1, index + 1) or
                     dfs(x - 1, y, index + 1) or
                     dfs(x, y - 1, index + 1))
            
            # Restore the original value of the cell (backtrack)
            board[x][y] = temp
            
            return found
        
        # Loop over each cell in the board to start the DFS from each cell
        for i in range(rows):
            for j in range(cols):
                # If the first character matches, start the DFS
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True
        
        # If no match is found after exploring all cells, return False
        return False
