class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[-1]*n for _ in range(n)]
        ans = 0

        for lenn in range(1,n+1):
            for i in range(n-lenn+1):
                j = i+lenn-1

                if lenn == 1:
                    dp[i][j] = True
                elif lenn == 2:
                    dp[i][j] = (s[i] == s[j])
                else:
                    dp[i][j] = s[i]==s[j] and dp[i+1][j-1]
                if dp[i][j]:
                    ans += 1
        return ans
