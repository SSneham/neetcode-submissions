class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r,d = [],[]
        n = len(senate)
        for i in range(n):
            if senate[i] == "R": r.append(i)
            else: d.append(i)
        
        while r and d:
            r_ind = r.pop(0)
            d_ind = d.pop(0)

            if r_ind<d_ind: r.append(r_ind+n)
            else: d.append(d_ind+n)
        return "Radiant" if r else "Dire"