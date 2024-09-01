class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:

        # Initialize pointers to the left and right edges of the matrix
        l = 0
        r = len(matrix) - 1  # r points to the last column/row index

        # Loop until the left pointer crosses the right pointer
        # Each iteration of the loop handles one "layer" of the matrix
        while l < r:

            # Iterate over the elements in the current layer
            # The number of elements to rotate in the current layer is (r - l)
            for i in range(r - l):

                # Define pointers for the top (t) and bottom (b) edges
                t = l  # t points to the first row of the current layer
                b = r  # b points to the last row of the current layer

                # Save the top-left element before it's overwritten
                topleft = matrix[t][l + i]

                # Perform the rotation by shifting elements in reverse order

                # Move the bottom-left element to the top-left position
                matrix[t][l + i] = matrix[b - i][l]

                # Move the bottom-right element to the bottom-left position
                matrix[b - i][l] = matrix[b][r - i]

                # Move the top-right element to the bottom-right position
                matrix[b][r - i] = matrix[t + i][r]

                # Move the saved top-left element to the top-right position
                matrix[t + i][r] = topleft

            # After completing one layer, move the left pointer inward and right pointer inward
            l += 1
            r -= 1

        # The loop continues until all layers are rotated.
