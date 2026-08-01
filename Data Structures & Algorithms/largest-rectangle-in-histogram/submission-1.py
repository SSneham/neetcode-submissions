class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        left, right = [-1]*n, [n]*n
        st = []

        for i in range(n):
            while st and heights[st[-1]]>=heights[i]:
                st.pop()
            if st:
                left[i] = st[-1]
            st.append(i)
        
        st = []

        for i in range(n-1,-1,-1):
            while st and heights[st[-1]]>=heights[i]:
                st.pop()
            if st:
                right[i] = st[-1]
            st.append(i)
        ans = 0
        for i in range(n):
            l,r = left[i]+1, right[i]-1
            ans = max(ans, heights[i] * (r-l+1))
        return ans
