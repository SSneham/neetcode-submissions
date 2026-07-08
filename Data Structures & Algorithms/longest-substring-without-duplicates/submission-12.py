class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n==0 or n==1:
            return n
        charset = set()
        l,r = 0,1
        charset.add(s[l])
        maxlen = 0

        while r<n:
            if s[r] not in charset:
                charset.add(s[r])
                print(s[r], (l,r))
                maxlen = max(maxlen, r-l+1)
                r += 1
            else:
                # while s[l] in charset and l<r:
                charset.remove(s[l])
                l += 1
        return maxlen
            

