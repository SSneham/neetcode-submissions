class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        maxsum,cursum = nums[0],0
        minsum, curmin = nums[0],1e9

        for num in nums:
            cursum = max(cursum+num, num)
            maxsum = max(maxsum, cursum)

            curmin = min(curmin+num, num)
            minsum = min(minsum, curmin)

        if maxsum<0: return maxsum
        return max(maxsum, sum(nums)-minsum)