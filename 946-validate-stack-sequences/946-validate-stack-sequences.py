class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        j=0
        st=[]
        for i in pushed:
            st.append(i)
            while st and st[-1]==popped[j]:
                j+=1
                st.pop()
                
        return True if j==len(popped) else False
        