class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Brute force - Generate all possible substrings
        n,m = len(s), len(t)
        if m>n: return ""

        minl = 1e9
        start = -1

        for i in range(n): #starting point can be any character
            hm = {}
            count = 0
            for j in range(m):
                hm[t[j]] = 1 + hm.get(t[j],0)
            
            # Now check for all substring starting with i which contains all the characters
            for j in range(i,n):
                if s[j] in hm: # if it is present in the hashmap
                    if hm[s[j]]>0:
                        count += 1
                    hm[s[j]] -= 1
                if count == m:
                    # Only change the start and the minl both if the new windpw length is smaller
                    if j-i+1<minl:
                        minl = j-i+1
                        start = i
                    break
        return "" if start == -1 else s[start:start+minl]

        