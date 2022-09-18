class Solution:
    def countSubstrings(self, s: str) -> int:
        ans=0
        for i in range(len(s)):
            ans+=self.helper(s,i,i)
            ans+=self.helper(s,i,i+1)
        return ans
        
    def helper(self,s,lo,hi):
        ans=0
        while lo>=0 and hi<len(s) and s[lo]==s[hi]:
            ans+=1
            lo-=1
            hi+=1
            
        return ans
        