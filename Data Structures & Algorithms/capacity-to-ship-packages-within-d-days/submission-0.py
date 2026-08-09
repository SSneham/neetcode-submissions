class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def condition(capacity):
            days = 1
            curr_wt = 0
            for w in weights:
                if curr_wt+w>capacity:
                    curr_wt = 0
                    days += 1
                curr_wt += w
            return days
        l,h = max(weights), sum(weights)
        ans = h
        while l<=h:
            m = l + (h-l)//2
            if condition(m) <= days:
                ans = m
                h = m-1
            else:
                l = m+1
        return ans