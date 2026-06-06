class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ans = []
        carry,addi = 0,0
        digits[-1] += 1
        for num in digits[::-1]:
            temp = num+carry
            addi = temp%10
            carry = temp//10
            ans.append(addi)
        if carry:
            ans.append(carry)
        return ans[::-1]