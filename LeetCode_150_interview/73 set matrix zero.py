class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])

        """first_row_zero = False
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
        #Brute force
        row=set()
        col=set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    row.add(i)
                    col.add(j)
        for i in range(m):
            for j in range(n):
                if i in row or j in col:
                    matrix[i][j]=0
        return matrix
        """
        # optimal approach
        col0=1
        for i in range(m):
            if matrix[i][0]==0:
                col0=0
            for j in range(1,n):
                if matrix[i][j]==0:
                    matrix[i][0]=0
                    matrix[0][j]=0
        for i in range(m-1,-1,-1):
            for j in range(n-1,0,-1):
                if matrix[i][0]==0 or matrix[0][j]==0:
                    matrix[i][j]=0
            if col0==0:
                matrix[i][0]=0
                
