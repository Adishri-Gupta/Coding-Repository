class Solution:
    def firstUniqChar(self, s: str) -> int:
        ctr=Counter(s)
        for i,string in enumerate(s):
            if ctr[string]==1:
                return i
        return -1
            
        