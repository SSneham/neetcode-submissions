class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Kadane's algorithm
        maxsum = nums[0]
        cursum = 0
        for num in nums:
            cursum += num
            maxsum = max(maxsum,cursum)
            if cursum<0:
                cursum = 0 
        return maxsum