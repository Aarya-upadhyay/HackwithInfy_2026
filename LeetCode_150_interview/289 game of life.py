class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row=len(board)
        col=len(board[0])
        dir=[(-1,-1),(-1,0),(-1,1),
             (0,-1)         ,(0,1),
             (1,-1),(1,0),(1,1)]
        for r in range(row):
            for c in range(col):
                l_n=0
                for dr,dc in dir:
                    nr,nc=r+dr,c+dc
                    if 0<=nr<row and 0<=nc<col:
                        if board[nr][nc]==1 or board[nr][nc]==2:
                            l_n+=1

                if board[r][c]==1:
                    if l_n<2 or l_n>3:
                        board[r][c]=2
                else:
                    if l_n==3:
                        board[r][c]=-1
        for r in range(row):
            for c in range(col):
                if board[r][c]==2:
                    board[r][c]=0
                elif board[r][c]==-1:
                    board[r][c]=1  
