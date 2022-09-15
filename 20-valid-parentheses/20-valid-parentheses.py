class Solution:
    def isValid(self, s: str) -> bool:
        bracket={')':'(','}':'{',']':'['}
        st=[]
        for sb in s:
            
            if sb in bracket:
            
               if st==[] or bracket[sb]!=st.pop():
                    return False        
            else:
                st.append(sb)
                
            
            
        return True if len(st)==0 else False