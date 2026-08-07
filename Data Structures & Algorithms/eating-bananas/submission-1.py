class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def bs(l,r):
            while l<r:
                m = l + (r-l)//2
                if condition(m):
                    r = m
                else:
                    l = m+1
            return l
        def condition(rate):
            ans = 0
            for pile in piles:
                ans += math.ceil(pile/rate)
            return ans <= h
        return bs(1,max(piles))