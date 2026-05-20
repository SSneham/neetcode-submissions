class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Brute force -> generate all subarrays and check
        # optimized -> keep a hashmap of prefix sums of the elements and if the there is are n number of subarrays with prefix sums (s-k), then there will be n number of subarrays with prefix sum k
        hm = {}
        hm[0] = 1
        presum = 0
        count = 0
        for num in nums:
            presum += num
            if presum-k in hm:
                count += hm[presum-k]
            hm[presum] = 1 + hm.get(presum,0)
        return count        



