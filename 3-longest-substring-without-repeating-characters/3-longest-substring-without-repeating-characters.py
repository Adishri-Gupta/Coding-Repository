class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start=0
        maxLen=-math.inf
        if len(s)==len(set(s)):
            return len(s)
        repeat={}
        for i in range(len(s)):
            if s[i] in repeat:
                start=max(start,repeat[s[i]]+1)
            maxLen=max(maxLen,i-start+1)
               
            repeat[s[i]]=i
        return maxLen