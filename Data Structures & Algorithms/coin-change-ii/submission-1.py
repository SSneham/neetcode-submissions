class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # if sum(coins)<amount: return 0
        n = len(coins)
        dp = [[-1]*(amount+1) for _ in range(n)]
        def f(i,remain):
            # base
            if i==n:
                return 0
            if remain == 0:
                return 1
            if dp[i][remain] != -1:
                return dp[i][remain]
            notpick = f(i+1, remain)
            pick = 0
            if coins[i]<=remain:
                pick = f(i, remain-coins[i])
            dp[i][remain] = pick+notpick
            return dp[i][remain]
        return f(0,amount)