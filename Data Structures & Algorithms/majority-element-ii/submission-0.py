class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # Brute Force
        n = len(nums)
        hm = {}
        for num in nums:
            hm[num] = 1 + hm.get(num,0)
        
        res = []
        for key,val in hm.items():
            if val>n//3:
                res.append(key)
        return res