class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #Brute force
        res = []
        n = len(nums)
        for i in range(n-k+1):
            window = nums[i:i+k]
            res.append(max(window))
        return res