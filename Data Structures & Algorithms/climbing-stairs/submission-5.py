class Solution:
    def climbStairs(self, n: int) -> int:
        # Memoization by striver's method
        # def f(n):
        #     if n<=1:
        #         return 1
        #     one = f(n-1)
        #     two = f(n-2)
        #     return one + two
        # return f(n)
        dp = [1]*(n+1)
        for i in range(2,n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]