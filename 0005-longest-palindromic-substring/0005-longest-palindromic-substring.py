class Solution:
    def longestPalindrome(self, s: str) -> str:
        res=''
        def isPalindrome(s,l,r):
            while l>=0 and r<len(s) and s[l]==s[r]:
                l-=1
                r+=1
            return s[l+1:r]
        
        for i in range(len(s)):
            
            temp=isPalindrome(s,i,i)
            if len(temp)>len(res):
                res=temp
            
            temp=isPalindrome(s,i,i+1)
            if len(temp)>len(res):
                res=temp
        return res
            
        
        
        
        