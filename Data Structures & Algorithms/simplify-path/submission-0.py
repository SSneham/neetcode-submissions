class Solution:
    def simplifyPath(self, path: str) -> str:
        st = []
        paths = path.split('/')

        for curr in paths:
            if curr == "..":
                if st:
                    st.pop()
            elif curr != "" and curr != ".":
                st.append(curr)
        return "/" + "/".join(st)