import sys
sys.setrecursionlimit(10000)
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [-1]*(n)
        # def f(ind):
        #     if ind >= n-1:
        #         dp[ind] = True
        #         return True
        #     if nums[ind] == 0:
        #         dp[ind] = False
        #         return False

        #     if dp[ind]!=-1: return dp[ind]

        #     val = nums[ind]
        #     ans = False
        #     for i in range(1,val+1):
        #         ans = ans or f(ind+i)
        #     dp[ind] = ans
        #     return ans
        # return f(0)

        #Tabulation
        # Base cases
        for ind in range(n):
            if nums[ind] == 0:
                dp[ind] = False
        dp[n-1] = True

        for ind in range(n-2,-1,-1):
            if dp[ind] == False: continue
            val = nums[ind]
            ans = False
            for i in range(1,val+1):
                if i<n:
                    ans = ans or dp[ind+i]
            dp[ind] = ans
        return dp[0]

                