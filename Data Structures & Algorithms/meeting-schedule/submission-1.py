"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, inter: List[Interval]) -> bool:
        inter = sorted(inter, key = lambda x : x.start)
        n = len(inter)

        for i in range(n-1):
            s1,e1 = inter[i].start, inter[i].end
            s2,e2 = inter[i+1].start, inter[i+1].end

            if s2<e1: return False
        return True