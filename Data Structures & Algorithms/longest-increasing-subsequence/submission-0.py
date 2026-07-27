class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[-1]*(n+1) for _ in range(n)]
        def f(i,j):
            if i==n:
                return 0
            if dp[i][j+1] != -1: return dp[i][j+1]
            curr = nums[i]
            pick = -1e9
            if j==-1 or curr>nums[j]:
                pick = 1 + f(i+1,i)
            notpick = f(i+1,j)
            dp[i][j+1] = max(pick,notpick)
            return dp[i][j+1]
        return f(0,-1)