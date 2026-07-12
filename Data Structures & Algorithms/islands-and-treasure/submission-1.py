from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m,n = len(grid), len(grid[0])
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        inf = 2**31-1
        visit = set()

        q = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append((i,j))
                    visit.add((i,j))
        
        while q:
            for _ in range(len(q)):
                x,y = q.popleft()
                for dx,dy in dirs:
                    nx,ny = x+dx,y+dy
                    if 0<=nx<m and 0<=ny<n and (nx,ny) not in visit and grid[nx][ny] == inf:
                        grid[nx][ny] = grid[x][y]+1
                        visit.add((nx,ny))
                        q.append((nx,ny))
        
