import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(x,y):
            return pow((x**2+y**2), 0.5)
        h = []
        for x,y in points:
            dist = -distance(x,y)
            heapq.heappush(h,(dist,[x,y]))
            if len(h)>k:
                heapq.heappop(h)
        ans = [ele[1] for ele in h]
        return ans
