class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Brute Force
        n = len(nums)
        # for i in range(n-1):
        #     for j in range(i+1,n):
        #         if j-i<=k and nums[i] == nums[j]:
        #             return True
        # return False

        # Using Hashmaps
        # hm = {}
        # for index,val in enumerate(nums):
        #     if val in hm and index - hm[val]<=k:
        #         return True
        #     else:
        #         hm[val] = index
        # return False

        # Using Sliding window
        # Assign l = 0, r = 1, then move the r pointer towards right, if it exceeds size k, increment l to decrease the window size, then compare with the condition to return true or false
        l,r = 0,0
        hs = set()
        while r<n:
            if r-l>k:
                hs.remove(nums[l])
                l += 1
            if nums[r] in hs:
                return True
            hs.add(nums[r])
            r += 1
        return False

        