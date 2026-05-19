class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # 2 pointer approach
        n = len(arr)
        l,r = 0,n-1

        while r-l>=k:
            if abs(x-arr[l]) <= abs(x-arr[r]):
                r -= 1
            else:
                l += 1
        return arr[l:r+1]
