sys.setrecursionlimit(20000)
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        if target%2 != 0:
            return False
        target //= 2

        n = len(nums)

        dp = {}

        def f(ind,res):
            if ind == -1:
                if res == target:
                    return True
                else:
                    return False
            if (ind,res) in dp:
                return dp[(ind,res)]
            not_take = f(ind-1,res)
            take = False
            if res+nums[ind] <= target:
                take = f(ind-1, res + nums[ind])
            dp[(ind,res)] = take or not_take
            return dp[(ind,res)]
        return f(n-1,0)
