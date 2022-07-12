class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans=[]
       
        
        def helper(S=[],left=0,right=0):
            if len(S)==2*n:
                ans.append("".join(S))
                return
            if left<n:
                S.append('(')
                helper(S,left+1,right)
                S.pop()
            if right<left:
                S.append(')')
                helper(S,left,right+1)
                S.pop()
        helper()
        return ans
                

    