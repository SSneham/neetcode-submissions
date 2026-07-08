class Solution:
    def longestCommonSubsequence(self, str1: str, str2: str) -> int:
        n,m = len(str1),len(str2)
        dp = [[-1]*m for _ in range(n)]
        def f(ind1, ind2):
            # Base case
            if ind1 == n or ind2 == m:
                return 0
            if dp[ind1][ind2] != -1:
                return dp[ind1][ind2]
            # Match
            if str1[ind1] == str2[ind2]:
                return f(ind1+1,ind2+1)+1
            # Not match
            left = f(ind1+1,ind2)
            right = f(ind1,ind2+1)
            dp[ind1][ind2] = max(left,right)
            return dp[ind1][ind2]
        return f(0,0)
