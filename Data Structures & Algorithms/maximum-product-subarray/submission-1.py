class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        ans = -float('inf')
        for i in range(n):
            prod = 1
            for j in range(i,n):
                prod *= nums[j]
                ans = max(ans,prod)
        return ans