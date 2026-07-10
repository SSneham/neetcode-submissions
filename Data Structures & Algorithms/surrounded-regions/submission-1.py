class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m,n = len(board), len(board[0])
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]

        def dfs(i,j):
            if i<0 or i==m or j<0 or j==n or board[i][j] != 'O':
                return
            board[i][j] = '#'
            for dx,dy in dirs:
                dfs(i+dx,j+dy)
        
        for j in range(n):
            if board[0][j] == 'O': dfs(0,j)
            if board[m-1][j] == 'O': dfs(m-1,j)

        for i in range(m):
            if board[i][0] == 'O': dfs(i,0)
            if board[i][n-1] == 'O': dfs(i,n-1)
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == '#':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'

        
