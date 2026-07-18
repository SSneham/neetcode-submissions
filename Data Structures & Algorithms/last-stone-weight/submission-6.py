import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = []
        for ele in stones:
            heapq.heappush(h,-ele)
        while len(h)>1:
            s1 = -heapq.heappop(h)
            s2 = -heapq.heappop(h)
            if s1>s2:
                heapq.heappush(h,-(s1-s2))
        return 0 if not h else -h[0]

