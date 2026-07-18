"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, inter: List[Interval]) -> bool:
        if not inter: return True
        inter.sort(key = lambda x:x.start)
        prevEnd = inter[0].end
        for i in range(1,len(inter)):
            if inter[i].start < prevEnd:
                return False
            else:
                prevEnd = inter[i].end
        return True