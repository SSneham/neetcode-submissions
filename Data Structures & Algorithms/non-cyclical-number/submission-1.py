class Solution:
    def isHappy(self, n: int) -> bool:
        summ = 0
        while n>0:
            rem = n%10
            summ += rem**2
            n //= 10
            if n==0 and summ>9:
                n = summ
                summ = 0
        return summ == 1