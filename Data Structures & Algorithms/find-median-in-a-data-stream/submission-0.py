class MedianFinder:

    def __init__(self):
        self.l = []        

    def addNum(self, num: int) -> None:
        self.l.append(num)
        self.l.sort()

    def findMedian(self) -> float:
        if len(self.l) == 1: return self.l[0]

        n = len(self.l)
        if n%2 != 0: return self.l[n//2]
        else: return (self.l[n//2-1]+self.l[n//2])/2
        