class Solution:
    def getSum(self, a: int, b: int) -> int:
        # xor -> gives the sum without carry
        # and and left shift gives the carry forward operation
        carry = 0
        res = 0
        mask = 0xffffffff

        for i in range(32):
            a_bit = (a>>i) & 1
            b_bit = (b>>i) & 1
            cur_bit = a_bit ^ b_bit ^ carry
            carry = (a_bit + b_bit + carry) >= 2
            if cur_bit:
                res |= (1<<i)
        if res>0x7fffffff:
            res = ~(res ^ mask)
        return res