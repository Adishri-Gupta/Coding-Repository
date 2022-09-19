class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        curr,prev=1,0
        ans=0
        for i in range(1,len(s)):
            if s[i]!=s[i-1]:
                ans+=min(curr,prev)
                prev=curr
                curr=1
            else:
                curr+=1
        return ans+min(curr,prev)
                