class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = -float('inf')
        n = len(nums)
        for i in range(n):
            summ = 0
            for j in range(i,n):
                summ += nums[j]
                maxsum = max(maxsum, summ)
        return maxsum