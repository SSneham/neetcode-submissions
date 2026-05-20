class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n,m = len(s),len(t)
        l,r,minl,count,start = 0,0,1e9,0,-1

        hm = [0]*256
        for ch in t: hm[ord(ch)] += 1

        while r<n:
            if hm[ord(s[r])]>0:
                count += 1
            hm[ord(s[r])] -= 1
                            
            while count == m:
                if r-l+1<minl:
                    minl = r-l+1
                    start = l

                hm[ord(s[l])] += 1

                if hm[ord(s[l])]>0:
                    count -= 1
                l += 1
                    
            r += 1
        return "" if start == -1 else s[start:start+minl]