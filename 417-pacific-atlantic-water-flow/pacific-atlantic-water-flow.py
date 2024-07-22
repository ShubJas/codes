"""
Approach:
To solve the problem of finding all cells in a matrix where water can flow to both the Pacific and Atlantic Oceans, we use a Depth-First Search (DFS) approach. The main idea is to perform DFS from the cells adjacent to the Pacific Ocean and the cells adjacent to the Atlantic Ocean, marking cells that can reach each ocean. Finally, the intersection of these two sets of cells gives us the cells that can flow to both oceans.

Steps:
1. Initialize the Data Structures: Create sets to keep track of cells that can reach the Pacific and Atlantic Oceans, respectively. Also, initialize a helper function `dfs` to perform DFS.
2. Perform DFS from Pacific Border: Perform DFS for each cell in the first row and the first column (these are the cells adjacent to the Pacific Ocean).
3. Perform DFS from Atlantic Border: Perform DFS for each cell in the last row and the last column (these are the cells adjacent to the Atlantic Ocean).
4. Find Intersection: The intersection of cells reachable from both oceans gives the required cells.
5. Return the Result: Convert the intersection to a list and return it.
"""

class Solution:
    def dfs(self, i, j, visited, heights):

        # Mark the current cell as visited
        visited.add((i, j))

        # Define the possible directions to move: down, right, up, left
        for (x, y) in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            # Calculate the new position based on the current direction
            dx = i + x
            dy = j + y
            # Check if the new position is within the bounds and not visited
            if 0 <= dx < self.rows and 0 <= dy < self.cols and (dx, dy) not in visited and heights[dx][dy] >= heights[i][j]:
                # Perform DFS on the new cell
                self.dfs(dx, dy, visited, heights)

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        # Get the number of rows and columns
        self.rows = len(heights)
        self.cols = len(heights[0])

        # Initialize sets to keep track of cells that can reach the Pacific and Atlantic Oceans
        pacific = set()
        atlantic = set()

        # Perform DFS from the Pacific Ocean border (first row and first column)
        for i in range(self.rows):
            self.dfs(i, 0, pacific, heights)
            self.dfs(i, self.cols - 1, atlantic, heights)

        # Perform DFS from the Atlantic Ocean border (last row and last column)
        for j in range(self.cols):
            self.dfs(0, j, pacific, heights)
            self.dfs(self.rows - 1, j, atlantic, heights)

        # Find the intersection of cells that can reach both oceans
        result = list(pacific & atlantic)

        # Return the result
        return result
