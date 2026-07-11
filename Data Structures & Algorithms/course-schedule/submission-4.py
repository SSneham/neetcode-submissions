from collections import defaultdict,deque 
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        V = numCourses
        adj = defaultdict(list)
        indegree = [0]*V
        for u,v in prerequisites:
            adj[v].append(u)
            indegree[u] += 1
        q = deque()
        for i in range(V):
            if indegree[i] == 0:
                q.append(i)
        seen = 0

        while q:
            for _ in range(len(q)):
                curr = q.popleft()
                seen += 1
                for nei in adj[curr]:
                    indegree[nei]-=1
                    if indegree[nei]==0:
                        q.append(nei)
        return seen == V
