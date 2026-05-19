class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Brute Force
        n = len(s)
        res = 0
        for i in range(n):
            hm = {}
            maxf = 0
            for j in range(i,n):
                hm[s[j]] = 1 + hm.get(s[j], 0)
                maxf = max(maxf, hm[s[j]])
                # print(maxf, end = " ")
                count = (j-i+1) - maxf
                # print(count)
                if count <= k:
                    res = max(res, j-i+1)
                else:
                    break # We break because we cannot shrink the string from the left ; i is fixed
        return res
