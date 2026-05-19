class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        l,r,summ,minl = 0,0,0,1e9
        while r<n:
            summ += nums[r]

            # Try shrinking the window
            while summ>=target:
                minl = min(minl, r-l+1)
                summ -= nums[l]
                l += 1
            r += 1
        return 0 if minl == 1e9 else minl