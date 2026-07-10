class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m,n = len(heights), len(heights[0])
        directions = [(-1,0),(1,0),(0,1),(0,-1)]
        atl,pac = set(),set()

        def dfs(i,j,prev,visit):
            if (
                (i,j) in visit or
                i<0 or j<0 or
                i==m or j==n or
                heights[i][j] < prev
            ):  return

            visit.add((i,j))
            for dx,dy in directions:
                dfs(i+dx, j+dy, heights[i][j], visit)
                
        for j in range(n):
            dfs(0,j,heights[0][j],pac)
            dfs(m-1,j,heights[m-1][j],atl)

        for i in range(m):
            dfs(i,0,heights[i][0],pac)
            dfs(i,n-1,heights[i][n-1],atl)
        return list(pac & atl) 