class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        # Brute force
        ans = 1
        n = len(arr)
        for i in range(n-1):
            count = 1
            if arr[i]<arr[i+1]:
                count += 1
                flag = 1 #1->greater
                j = i+1
                while j<n-1:
                    if flag == 1:
                        if arr[j]>arr[j+1]:
                            flag = 0
                            count += 1
                            j += 1
                        else: break
                    elif flag == 0:
                        if arr[j]<arr[j+1]:
                            flag = 1
                            count += 1
                            j += 1
                        else: break
                ans=max(ans,count)
            elif arr[i]>arr[i+1]:
                count += 1
                flag = 0 #0->lesser
                j = i+1
                while j<n-1:
                    if flag == 1:
                        if arr[j]>arr[j+1]:
                            flag = 0
                            count += 1
                            j += 1
                        else: break
                    elif flag == 0:
                        if arr[j]<arr[j+1]:
                            flag = 1
                            count += 1
                            j += 1
                        else: break
                ans=max(ans,count)
            else:
                continue
        return ans