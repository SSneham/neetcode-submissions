class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {}
        for i,val in enumerate(s):
            last[val] = i
        
        n = len(s)
        start = end = 0
        res = []
        for i in range(n):
            end = max(end,last[s[i]])
            if i==end:
                res.append(end-start+1)
                start = end + 1
        return res