class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        dp = [[-1]*n for _ in range(m)]
        def f(i,j):
            #base case
            if i==0 and j==0:
                return grid[i][j]
            if dp[i][j] != -1:
                return dp[i][j]
            up = left = 1e9
            if i-1>=0:
                up = f(i-1,j)
            if j-1>=0:
                left = f(i,j-1)
            dp[i][j] = grid[i][j] + min(up,left)
            return dp[i][j]
        return f(m-1,n-1)