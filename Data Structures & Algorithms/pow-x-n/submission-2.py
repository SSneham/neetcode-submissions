class Solution:
    def myPow(self, x: float, n: int) -> float:
        def f(x,n):
            if x==0:
                return 0
            if n==0:
                return 1
            if n%2:
                return f(x*x, n//2)*x
            return f(x*x, n//2)
            # temp = f(x*x, n//2)
            # return temp*x if n%2 else temp
        return f(x,abs(n)) if n>0 else 1/f(x,abs(n))