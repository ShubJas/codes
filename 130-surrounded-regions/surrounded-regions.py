class Solution:
    def dfs(self,board,i,j):
        

        if i < 0 or j< 0 or i >= self.rows or j >=self.cols or board[i][j] != "O":
            return


        board[i][j] = '.'

        self.dfs(board,i+1,j)
        self.dfs(board,i-1,j)   
        self.dfs(board,i,j+1)   
        self.dfs(board,i,j-1)   

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        self.rows = len(board)
        self.cols = len(board[0])
        for i in range(self.rows):
            for j in range(self.cols):
                if i == 0 or j == 0 or i == self.rows-1 or j == self.cols -1:
                    self.dfs(board,i,j)
        
        for i in range(self.rows):
            for j in range(self.cols):
                if board[i][j]!='.':
                    board[i][j] = "X"
                else:
                    board[i][j] = "O"