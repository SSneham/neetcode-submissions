class Solution:
    def romanToInt(self, s: str) -> int:
        n = len(s)
        hm = {'I':1,'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        ans = 0

        i = 0
        while i<n:
            if i<n-1 and s[i] == 'I':
                if s[i+1] == 'V' or s[i+1] == 'X':
                    ans += hm[s[i+1]] - 1
                    i += 2
                else:
                    ans += hm[s[i]]
                    i += 1
            
            elif i<n-1 and s[i] == 'X':
                if s[i+1] == 'L' or s[i+1] == 'C':
                    ans += hm[s[i+1]] - 10
                    i += 2
                else:
                    ans += hm[s[i]]
                    i += 1
            
            elif i<n-1 and s[i] == 'C':
                if s[i+1] == 'D' or s[i+1] == 'M':
                    ans += hm[s[i+1]] - 100
                    i += 2
                else:
                    ans += hm[s[i]]
                    i += 1          
            else:
                ans += hm[s[i]] 
                i += 1
        return ans
                     