class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        def expand(l,r):
            # if both strings are equal, expand outwards
            while l>=0 and r<n:
                if s[l]==s[r]:
                    l -= 1
                    r += 1
                else:
                    break
            return l+1, r-1

        start, end = 0,0
        for i in range(n):
            # for single character center
            l1,r1 = expand(i-1,i+1)
            if r1-l1>end-start:
                start,end = l1,r1
            # for even length character
            l2,r2 = expand(i,i+1)
            if r2-l2>end-start:
                start,end = l2,r2

        return s[start:end+1]
            
            
