class Solution:
    def decodeString(self, s: str) -> str:
        st = []
        for ch in s:
            if ch == ']':
                ele = ""
                while st and st[-1] != '[':
                    ele = st.pop() + ele
                st.pop()

                num = ""
                while st and st[-1].isdigit():
                    num = st.pop() + num
                num = int(num)
                st.append(ele*num)
            else:
                st.append(ch)
        ans = ""
        for ele in st: ans += ele
        return ans