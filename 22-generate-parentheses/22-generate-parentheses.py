class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.res=[]
        self.n = 2*n
        self.helper('',0)
        
        return self.res
    def helper(self, currComb,openB):
        if len(currComb) == self.n:
            if openB==0 :
                self.res.append(currComb)
            return
      
        self.helper(currComb+'(',openB+1)
     
        if openB:
         
            self.helper(currComb+')',openB-1)