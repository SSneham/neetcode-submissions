class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n,m = len(s1), len(s2)
        s1 = sorted(s1)
        for i in range(m-n+1):
            substr = s2[i:i+n]
            if sorted(substr) == s1:
                return True
        return False