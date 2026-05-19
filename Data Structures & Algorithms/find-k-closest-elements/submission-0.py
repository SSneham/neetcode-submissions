class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # condition : closest when 1. abs diff is less or 2. if abs diff is same, then a<b
        def sortt(i):
            return abs(i-x)

        sorted_arr = sorted(arr, key = sortt)
        return sorted(sorted_arr[:k])