class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []
        for ast in asteroids:
            while st and st[-1]>0 and ast<0:
                if st[-1]<-ast:
                    st.pop()
                elif st[-1]>-ast:
                    ast = 0
                else:
                    st.pop()
                    ast = 0
            if ast:
                st.append(ast)
        return st