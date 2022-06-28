class Solution:
    def findAnagrams(self, s2: str, s1: str) -> List[int]:
        freq1 = [0] * 26
        freq2 = [0] * 26
        j=0
        res=[]
        n=len(s1)
        if len(s2) < len(s1):
            return []
        for i in s1:
            freq1[ord(i) - ord('a')] += 1
            freq2[ord(s2[j]) - ord('a')] += 1
            j += 1
        if freq2==freq1:
            res.append(0)
        for i in range(len(s2)-len(s1)):
            
            freq2[ord(s2[i+n])-ord('a')]+=1
            freq2[ord(s2[i])-ord('a')]-=1
            if freq2==freq1:
                res.append(i+1)
        return res
        
            