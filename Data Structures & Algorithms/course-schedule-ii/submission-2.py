class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
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
        seen = []

        while q:
            for _ in range(len(q)):
                curr = q.popleft()
                seen.append(curr)
                for nei in adj[curr]:
                    indegree[nei]-=1
                    if indegree[nei]==0:
                        q.append(nei)
        return seen if len(seen) == V else []
