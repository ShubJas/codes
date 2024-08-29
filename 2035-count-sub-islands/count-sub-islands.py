from typing import List

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        n = len(grid1)
        m = len(grid1[0])

        visited = [[False] * m for _ in range(n)]

        def dfs(x, y) -> bool:
            # Base case: if out of bounds, or already visited, or not part of an island in grid2, return True
            if x < 0 or x >= n or y < 0 or y >= m or visited[x][y] or grid2[x][y] != 1:
                return True
            
            visited[x][y] = True

            # If this cell is land in grid2 but not in grid1, it's not a sub-island
            is_sub_island = grid1[x][y] == 1

            # Explore all four directions - cant do one return as we have to explore
            # Even if one direction returns False, the entire island can't be a sub-island
            is_sub_island = dfs(x+1, y) and is_sub_island
            is_sub_island = dfs(x-1, y) and is_sub_island
            is_sub_island = dfs(x, y+1) and is_sub_island
            is_sub_island = dfs(x, y-1) and is_sub_island

            return is_sub_island

        count = 0
        for i in range(n):
            for j in range(m):
                # Start a DFS if we find an unvisited land cell in grid2
                if grid2[i][j] == 1 and not visited[i][j]:
                    # Increment the count if the DFS confirms that the island is a sub-island
                    count += dfs(i, j)

        return count
