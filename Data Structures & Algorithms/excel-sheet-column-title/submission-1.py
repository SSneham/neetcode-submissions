class Solution:
    def convertToTitle(self, n: int) -> str:
        res = ""
        while n:
            n -= 1
            temp = n%26 + ord('A')
            res += chr(temp)
            n = int(n/26)
        return res[::-1]
        