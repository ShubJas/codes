class Solution:
    def dfs(self, board, i, j):
        # If out of bounds or the cell is not 'O', stop the DFS
        if i < 0 or j < 0 or i >= self.rows or j >= self.cols or board[i][j] != "O":
            return
        
        # Mark the current cell as visited by setting it to '.'
        board[i][j] = '.'

        # Explore all four directions: down, up, right, left
        self.dfs(board, i + 1, j)
        self.dfs(board, i - 1, j)   
        self.dfs(board, i, j + 1)   
        self.dfs(board, i, j - 1)   

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # Initialize the number of rows and columns
        self.rows = len(board)
        self.cols = len(board[0])

        # Perform DFS from all 'O's on the boundary
        for i in range(self.rows):
            for j in range(self.cols):
                # If the cell is on the boundary and is 'O', start DFS
                if i == 0 or j == 0 or i == self.rows - 1 or j == self.cols - 1:
                    self.dfs(board, i, j)
        
        # Process the entire board and convert the cells based on DFS results
        for i in range(self.rows):
            for j in range(self.cols):
                if board[i][j] != '.':
                    # If the cell is not '.', it means it was not connected to a boundary 'O'
                    board[i][j] = "X"
                else:
                    # If the cell is '.', it means it was connected to a boundary 'O'
                    board[i][j] = "O"
