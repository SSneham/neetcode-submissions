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
                lmin -= 1
                lmax += 1
            if lmax<0: return False
            if lmin<0:
                lmin = 0
        # print(lmin,lmax)
        return lmin == 0