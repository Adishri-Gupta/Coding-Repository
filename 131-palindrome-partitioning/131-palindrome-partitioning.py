class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.res=[]
        self.helper(0,[],s)
        return self.res
    def helper(self,start,currComb,s):
        
        if start==len(s):
            self.res.append(list(currComb))
            return
        for i in range(start,len(s)):
            if self.isPal(s[start:i+1]):
                currComb.append(s[start:i+1])
                self.helper(i+1,currComb,s)
                currComb.pop()
            
    def isPal(self,strCheck):
        if strCheck==strCheck[::-1]:
            return True