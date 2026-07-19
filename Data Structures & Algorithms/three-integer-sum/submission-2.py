class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n):
            if i>0 and nums[i-1] == nums[i]:
                continue
            t = -nums[i]
            l,r = i+1,n-1
            while l<r:
                summ = nums[l]+nums[r]
                if summ<t:
                    l += 1
                elif summ>t:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l<r and nums[l-1] == nums[l]:
                        l += 1
                    while l<r and nums[r] == nums[r+1]:
                        r -= 1
        return res