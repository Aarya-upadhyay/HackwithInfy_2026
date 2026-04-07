class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """n=len(board)
        m=len(board[0])
        for i in range(n):
            seen=[]
            for j in range(m):
                if board[i][j]!='.':
                    if board[i][j] in seen:
                        return False
                    seen.append(board[i][j])
        for j in range(9):
            seen=[]
            for i in range(9):
                if board[i][j]!='.':
                    if board[i][j] in seen:
                        return False
                    seen.append(board[i][j])
        for b in range(0,9,3):
            for c in range(0,9,3):
                seen = []
                for i in range(3):
                    for j in range(3):
                        val = board[b+i][c+j]
                        if val != '.':
                            if val in seen:
                                return False
                            seen.append(val)
        return True
"""
        cols, rows, sq = defaultdict(set), defaultdict(set), defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".": continue
                
                if (board[r][c] in rows[r] or 
                board[r][c] in cols[c] or 
                board[r][c] in sq[(r//3, c//3)]):
                    return False
                
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                sq[(r//3, c//3)].add(board[r][c])

        # print(cols, rows, sq)
        return True

                    
