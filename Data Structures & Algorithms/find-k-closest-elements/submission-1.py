class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # condition : closest when 1. abs diff is less or 2. if abs diff is same, then a<b
        n = len(arr)
        diff = [0]*k
        res = [0]*k
        j = 0
    
        for i in range(k):
            diff[i] = abs(arr[i]-x)
            res[i] = arr[i]
        maxdiff = max(diff)
    
    
        for i in range(k,n):
            if abs(arr[i]-x)<maxdiff:
                diff[j] = abs(arr[i]-x)
                res[j] = arr[i]
                maxdiff = max(diff)
                j = (j+1)%k
        return sorted(res)
    
    