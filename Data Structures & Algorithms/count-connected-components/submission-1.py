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
                return
            elif rank[par_i] > rank[par_j]:
                parent[par_j] = par_i
            elif rank[par_i] < rank[par_j]:
                parent[par_i] = par_j
            else:
                parent[par_i] = par_j
                rank[par_j] += 1
        parent = list(range(n))
        rank = [0]*n
        for i,j in edges:
            union(i,j,parent,rank)
       
        seen = set()
        for ele in parent:
            par = find(ele,parent)
            if par not in seen:
                seen.add(par)
        return len(seen)