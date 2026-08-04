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
            r -= 1
            l += 1
            return l,r
        ans = ""
        maxlen = 0
        for i in range(n):
            # for single character center
            l1,r1 = expand(i-1,i+1)
            # for even length character
            l2,r2 = expand(i,i+1)
            
            #compare lenghts
            oddlen = r1-l1+1
            evenlen = r2-l2+1

            if oddlen>maxlen:
                maxlen = oddlen
                ans = s[l1:r1+1]
            if evenlen>maxlen:
                maxlen = evenlen
                ans = s[l2:r2+1]

        return ans
            
            
