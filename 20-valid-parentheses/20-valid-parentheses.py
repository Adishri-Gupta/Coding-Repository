class Solution:
    def isValid(self, s: str) -> bool:
        mappings={')':'(',']':'[','}':'{'}
        st=[]
        for c in s:
            if c in mappings:
                if st==[] or st.pop()!=mappings[c]:
                    return False
                   
            else:
                st.append(c)
        return True if st==[] else False
                
        