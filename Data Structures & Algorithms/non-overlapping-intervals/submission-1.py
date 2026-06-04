class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        prevEnd = intervals[0][1]

        for s,e in intervals[1:]:
            #If they do not overlap, just update the prevEnd
            if s>=prevEnd:
                prevEnd = e
            else:
                # They do overlap, increment the count of res, update the prevEnd
                res += 1
                prevEnd = min(prevEnd, e)
        return res