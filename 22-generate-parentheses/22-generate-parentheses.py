class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.res=[]
        self.n = 2*n
        self.helper('',[])
        
        return self.res
    def helper(self, currComb,st):
        
        if len(currComb) == self.n:
            if len(st)==0 :
                self.res.append(currComb)
            return
       
        st.append('(')
        self.helper(currComb+'(',st)
        st.pop()
        
        if st and st[-1]=='(':
            st.pop()
            self.helper(currComb+')',st)
            st.append('(')