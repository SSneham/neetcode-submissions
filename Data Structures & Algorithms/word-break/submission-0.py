class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = {}

        def f(i):
            if i == len(s):
                return True
            if i in dp:
                return dp[i]
            
            for word in wordDict:
                if s.startswith(word,i):
                    if f(i+len(word)):
                        dp[i] = True
                        return True
            dp[i] = False
            return False
        return f(0)
