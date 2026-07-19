class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        n = len(word)

        def dfs(ind,r,c):
            if ind == n:
                return True
            if (r<0 or r>=rows or
                c<0 or c>=cols or
                board[r][c] != word[ind]
            ): return False

            temp = board[r][c]
            board[r][c] = '#'
            # found = False
            found = (
                dfs(ind+1,r+1,c) or
                dfs(ind+1,r-1,c) or
                dfs(ind+1,r,c+1) or
                dfs(ind+1,r,c-1)
            )
            board[r][c] = temp
            return found
        
        for i in range(rows):
            for j in range(cols):
                if dfs(0,i,j):
                    return True
        return False
