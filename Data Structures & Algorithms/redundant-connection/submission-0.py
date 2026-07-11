class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        def find(i,parent):
            if i==parent[i]: return i
            parent[i] = find(parent[i],parent)
            return parent[i]

        def union(i,j,parent,rank):
            par_i = find(i,parent)
            par_j = find(j,parent)

            if par_i == par_j:
                return True
            elif rank[par_i] > rank[par_j]:
                parent[par_j] = par_i
            elif rank[par_i] < rank[par_j]:
                parent[par_i] = par_j
            else:
                parent[par_i] = par_j
                rank[par_j] += 1
            return False
        parent = list(range(n+1))
        rank = [0]*(n+1)
        
        for i,j in edges:
            if union(i,j,parent,rank):
                return [i,j]