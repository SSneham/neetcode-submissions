class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        curr = intervals[0]
        res = []
        n = len(intervals)
        for i in range(1,n):
            #If curr ends before interval[i] starts:
            if curr[1]<intervals[i][0]:
                res.append(curr)
                curr = intervals[i]
            elif curr[0]>intervals[i][1]:
                res.append(intervals[i])
            else:
                # The intervals overlap
                curr = [min(intervals[i][0], curr[0]), max(intervals[i][1], curr[1])]
        res.append(curr)
        return res
            
            