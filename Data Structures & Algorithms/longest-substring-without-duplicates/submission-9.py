class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        charSet = set()
        l,maxlen = 0,0
        for r in range(n):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            maxlen = max(maxlen,r-l+1)
        return maxlen

