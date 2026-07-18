from collections import Counter,deque
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        maxh = [count for count in counter.values()]
        heapq.heapify_max(maxh)

        q = deque() # [count, next_available_time]
        time = 0

        while maxh or q:
            time += 1
            if maxh:
                count = heapq.heappop_max(maxh) - 1
                if count:
                    q.append([count, time+n])
            if q and q[0][1] == time:
                heapq.heappush_max(maxh, q.popleft()[0])
        return time