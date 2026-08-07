class Solution:
    def mySqrt(self, x: int) -> int:
        if x<2:
            return x
        l,r = 0,x
        while l<r:
            m = (l+r)//2
            if m*m > x:
                r = m
            else:
                l = m+1
        return l-1