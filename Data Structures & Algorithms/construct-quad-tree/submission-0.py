"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)
        def isSame(grid,x,y,n):
            unit = grid[x][y]
            for r in range(x,x+n):
                for c in range(y,y+n):
                    if grid[r][c]!=unit: return False
            return True
        
        def solve(grid,x,y,n):
            if isSame(grid,x,y,n):
                return Node(grid[x][y], True, None, None, None, None)
            else:
                node = Node(1,False,None,None,None,None)
                node.topLeft = solve(grid,x,y,n//2)
                node.topRight = solve(grid,x,y+n//2,n//2)
                node.bottomLeft = solve(grid,x+n//2,y,n//2)
                node.bottomRight = solve(grid,x+n//2,y+n//2,n//2)
                return node
        return solve(grid,0,0,n)