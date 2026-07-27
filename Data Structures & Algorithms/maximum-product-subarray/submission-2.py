class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curmin, curmax = 1,1

        for num in nums:
            temp = curmax*num
            curmax = max(temp,num*curmin,num)
            curmin = min(temp,num*curmin,num)
            res = max(res,curmax)
        return res
            