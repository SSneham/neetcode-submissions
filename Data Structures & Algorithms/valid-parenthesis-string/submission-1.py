class Solution:
    def checkValidString(self, s: str) -> bool:
        lmin, lmax = 0,0
        for ch in s:
            if ch == '(':
                lmin += 1
                lmax += 1
            elif ch == ')':
                lmin -= 1
                lmax -= 1
            else:
                lmin = (lmin-1) if lmin>1 else 0
                lmax += 1
            if lmax<0: return False
        return 0 in range(lmin, lmax+1)