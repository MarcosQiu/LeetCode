class Solution:
    '''
    54. Spiral Matrix
    recursion
    '''
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = list()
        rows = len(matrix)
        cols = len(matrix[0])
        self.spiralOrderOuterLayer(matrix, (0, 0), (rows - 1, cols - 1), result)

        return result

    def spiralOrderOuterLayer(self, matrix, top_left, bottom_right, current_sequence):
        top_left_row, top_left_col = top_left
        bottom_right_row, bottom_right_col = bottom_right
        
        if top_left_row < bottom_right_row and top_left_col < bottom_right_col:
            for col in range(top_left_col, bottom_right_col):
                current_sequence.append(matrix[top_left_row][col])
            for row in range(top_left_row, bottom_right_row):
                current_sequence.append(matrix[row][bottom_right_col])
            for col in range(bottom_right_col, top_left_col, -1):
                current_sequence.append(matrix[bottom_right_row][col])
            for row in range(bottom_right_row, top_left_row, -1):
                current_sequence.append(matrix[row][top_left_col])
            self.spiralOrderOuterLayer(
                matrix,
                (top_left_row + 1, top_left_col + 1),
                (bottom_right_row - 1, bottom_right_col - 1),
                current_sequence
            )
        elif top_left_col == bottom_right_col:
            for row in range(top_left_row, bottom_right_row + 1):
                current_sequence.append(matrix[row][top_left_col])
        elif top_left_row == bottom_right_row:
            for col in range(top_left_col, bottom_right_col + 1):
                current_sequence.append(matrix[top_left_row][col])