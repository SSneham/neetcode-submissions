class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        def find(i,parent):
            if i==parent[i]: return i
            parent[i] = find(parent[i],parent)
            return parent[i]

        def union(i,j,parent,rank):
            par_i = find(i,parent)
            par_j = find(j,parent)

            if par_i == par_j:
                return False
            elif rank[par_i] > rank[par_j]:
                parent[par_j] = par_i
            elif rank[par_i] < rank[par_j]:
                parent[par_i] = par_j
            else:
                parent[par_i] = par_j
                rank[par_j] += 1
            return True
        parent = list(range(n))
        rank = [0]*n
        ans = n
        for i,j in edges:
            if union(i,j,parent,rank):
                ans -= 1
        return ans
       
