import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}
        for num in nums:
            hm[num] = 1 + hm.get(num,0)
        h = []
        for key in hm:
            heapq.heappush(h,(hm[key], key))
        while len(h)>k:
            heapq.heappop(h)
        
        ans = []
        for ele in h:
            ans.append(ele[1])
        return ans
        