class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n=len(s)
        dp = [False]*n
     
        for i in range(n):
            for word in wordDict:
                if word==s[i-len(word)+1:i+1] and (dp[i-len(word)]==True or i-len(word)==-1):
                    dp[i]=True
        return dp[-1]
                