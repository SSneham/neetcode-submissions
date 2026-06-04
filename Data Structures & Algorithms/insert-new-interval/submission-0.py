class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        n = len(intervals)
        for i in range(n):
            # If the new Interval ends before inter[i] begins:
            if newInterval[1]<intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            # Else if the new Interval begins after the current interval ends
            elif intervals[i][1]<newInterval[0]:
                res.append(intervals[i])
            else:
                # The intervals overlap
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        res.append(newInterval)
        return res