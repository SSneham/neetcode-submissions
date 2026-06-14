from collections import defaultdict
class CountSquares:

    def __init__(self):
        # self.points = []
        self.hm = {}

    def add(self, point: List[int]) -> None:
        # self.points.append(point)
        self.hm[tuple(point)] = 1+self.hm.get(tuple(point),0)

    def count(self, point: List[int]) -> int:
        res = 0
        px,py = point
        for x,y in self.hm:
            if (abs(px-x) != abs(py-y)) or px == x or py == y:
                continue
            else:
                res += (
                self.hm[(x, y)]
                * self.hm.get((px, y), 0)
                * self.hm.get((x, py), 0)
            )
        return res
