from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m,n = len(grid), len(grid[0])
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        visit = set()

        def addEdge(i,j):
            if i<0 or i==m or j<0 or j==n or grid[i][j] == -1 or (i,j)in visit:
                return
            q.append((i,j))
            visit.add((i,j))
        
        q = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append((i,j))
                    visit.add((i,j))
        
        dist = 0
        while q:
            for _ in range(len(q)):
                x,y = q.popleft()
                grid[x][y] = dist
                for dx,dy in dirs:
                    addEdge(x+dx,y+dy)
            dist += 1
        
