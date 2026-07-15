from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = Counter(nums)
        n = len(nums)
        for key in counter:
            if counter[key] > n/2:
                return key