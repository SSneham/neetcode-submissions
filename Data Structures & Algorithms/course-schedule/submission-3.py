from collections import defaultdict 
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for u,v in prerequisites:
            adj[v].append(u)
        rec_stack = set()
        visited = set()

        def dfs(node):
            visited.add(node)
            rec_stack.add(node)

            for nei in adj[node]:
                if nei not in visited:
                    if dfs(nei):
                        return True
                elif nei in rec_stack:
                    return True
            rec_stack.remove(node)
            return False 
        for i in range(numCourses):
            if i not in visited:
                if dfs(i):
                    return False
        return True
        