class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Divide and Conquer
        def dfs(l,r):
            if l>r:
                return -float('inf')
            
            ls = rs = cs = 0
            m = (l+r)//2
            for i in range(m-1,l-1,-1):
                cs += nums[i]
                ls = max(ls,cs)
            cs = 0
            for i in range(m+1,r+1,1):
                cs += nums[i]
                rs = max(rs,cs)
            return max(
                dfs(l,m-1),
                dfs(m+1,r),
                ls+nums[m]+rs
            )
        return dfs(0,len(nums)-1)
        