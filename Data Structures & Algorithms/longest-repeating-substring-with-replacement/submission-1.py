from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Brute Force
        n = len(s)
        l = r = maxf = maxlen = 0
        hm = defaultdict(int)

        while r<n:
            hm[s[r]] += 1
            maxf = max(maxf, hm[s[r]])

            count = (r-l+1) - maxf
            #check for violation
            if count>k:
                while count>k:
                    hm[s[l]] -= 1
                    maxf = max(hm.values())
                    # Always increment l after decreasing the frequency of it, not vice versa
                    l += 1
                    count = (r-l+1) - maxf
            else:
                # substring is valid, update the maxlen
                maxlen = max(maxlen, r-l+1)
            r += 1
        return maxlen