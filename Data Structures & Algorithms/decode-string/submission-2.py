class Solution:
    def decodeString(self, s: str) -> str:
        st = []
        for ch in s:
            if ch == ']':
                ele = ""
                while st and st[-1] != '[':
                    ele += st.pop()[::-1]
                ele = ele[::-1]
                st.pop()

                num = ""
                while st and st[-1].isdigit():
                    num += st.pop()
                num = int(num[::-1])
                st.append(ele*num)
                print(st)
            else:
                st.append(ch)
        ans = ""
        for ele in st: ans += ele
        return ans