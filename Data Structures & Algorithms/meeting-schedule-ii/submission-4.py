"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        events = []
        for i in intervals:
            events.append((i.start,+1))
            events.append((i.end,-1))
        events.sort()
        overlap,maxi = 0,0

        for event in events:
            overlap += event[1]
            maxi = max(maxi,overlap)
        return maxi