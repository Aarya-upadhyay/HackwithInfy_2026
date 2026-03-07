Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
You must do it in place.

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])

        first_row_zero = False
        first_col_zero = False

        # Check first row
        for j in range(n):
            if matrix[0][j] == 0:
                first_row_zero = True

        # Check first column
        for i in range(m):
            if matrix[i][0] == 0:
                first_col_zero = True

        # Use first row and column as markers
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Set cells to zero based on markers
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Fix first row
        if first_row_zero:
            for j in range(n):
                matrix[0][j] = 0

        # Fix first column
        if first_col_zero:
            for i in range(m):
                matrix[i][0] = 0     
        
