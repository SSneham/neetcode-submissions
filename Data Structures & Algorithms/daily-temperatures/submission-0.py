class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0]*n
        st = [n-1]

        for i in range(n-2,-1,-1):
            temp = temperatures[i]
            # print(st)
            while st and temperatures[st[-1]] <= temp:
                st.pop()
            if st:
                ans[i] = st[-1]-i
            st.append(i)
        return ans