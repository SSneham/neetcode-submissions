class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        # Swap if needed, make num1 > num2 (in length)
        if len(num2)>len(num1):
            num1,num2 = num2,num1
        def mul(a,b):
            a,b = int(a),int(b)
            res = a*b
            return res
        ans = 0
        for i in num2:
            temp = mul(num1,i)
            ans = ans*10 + temp
        return str(ans)