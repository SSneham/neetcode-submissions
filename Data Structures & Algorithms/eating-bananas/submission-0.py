class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def req(k):
            total = 0
            for pile in piles:
                total += math.ceil(pile/k)
            return total
        l,r = 1, max(piles)
        while l<=r:
            m = l + (r-l)//2
            time = req(m)
            if time <= h:
                r = m-1
            elif time > h:
                l = m+1
        return l