class Solution:
    def dfs(self, image, i, j, val, color):
        # Base case: if the current cell is out of bounds or not equal to the original color
        if i < 0 or j < 0 or i >= self.rows or j >= self.cols or image[i][j] != val:
            return
        
        # Change the color of the current cell to the target color
        image[i][j] = color

        # Recursively call dfs for all 4 directions
        self.dfs(image, i + 1, j, val, color)  # Move down
        self.dfs(image, i - 1, j, val, color)  # Move up
        self.dfs(image, i, j + 1, val, color)  # Move right
        self.dfs(image, i, j - 1, val, color)  # Move left

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # Get the dimensions of the image
        self.rows = len(image)
        self.cols = len(image[0])
        
        # Get the original color of the starting pixel
        original_color = image[sr][sc]

        # If the original color is the same as the target color, no need to fill
        if original_color == color:
            return image

        # Start the DFS from the starting pixel
        self.dfs(image, sr, sc, original_color, color)
        
        return image
