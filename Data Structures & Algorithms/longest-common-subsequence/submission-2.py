class Solution:
    def longestCommonSubsequence(self, str1: str, str2: str) -> int:
        n,m = len(str1), len(str2)
        dp = [[-1]*m for _ in range(n)]
        def f(ind1, ind2):
            #base case
            if ind1==-1 or ind2==-1:
                return 0
            if dp[ind1][ind2] != -1:
                return dp[ind1][ind2]
            match = notmatch = -1e9
            #match
            if str1[ind1] == str2[ind2]: match = 1 + f(ind1-1,ind2-1)
            #not match
            else: notmatch = max(f(ind1-1,ind2),f(ind1,ind2-1))
            dp[ind1][ind2] = max(match, notmatch)
            return dp[ind1][ind2]
        return f(n-1,m-1)