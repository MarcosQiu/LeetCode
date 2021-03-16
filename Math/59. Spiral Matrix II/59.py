class Solution:
    '''
    59. Spiral Matrix II
    '''
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = list()
        for _ in range(n):
            matrix.append([0] * n)

        def fill(top_left, bottom_right, number_to_fill):
            if top_left == bottom_right:
                row, col = top_left
                matrix[row][col] = number_to_fill
            elif top_left[0] < bottom_right[0]:
                top_left_row, top_left_col = top_left
                bottom_right_row, bottom_right_col = bottom_right

                for col in range(top_left_col, bottom_right_col):
                    matrix[top_left_row][col] = number_to_fill
                    number_to_fill += 1
                for row in range(top_left_row, bottom_right_row):
                    matrix[row][bottom_right_col] = number_to_fill
                    number_to_fill += 1
                for col in range(bottom_right_col, top_left_col, -1):
                    matrix[bottom_right_row][col] = number_to_fill
                    number_to_fill += 1
                for row in range(bottom_right_row, top_left_row, -1):
                    matrix[row][top_left_col] = number_to_fill
                    number_to_fill += 1
                fill(
                    (top_left_row + 1, top_left_col + 1),
                    (bottom_right_row - 1, bottom_right_col - 1),
                    number_to_fill
                )
        
        fill((0, 0), (n - 1, n - 1), 1)
        return matrix