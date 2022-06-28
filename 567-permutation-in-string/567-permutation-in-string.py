class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        freq1 = [0] * 26
        freq2 = [0] * 26
        j=0
        n=len(s1)
        if len(s2) < len(s1):
            return False
        for i in s1:
            freq1[ord(i) - ord('a')] += 1
            freq2[ord(s2[j]) - ord('a')] += 1
            j += 1
        if freq2==freq1:
                return True
        for i in range(len(s2)-len(s1)):
            
            freq2[ord(s2[i+n])-ord('a')]+=1
            freq2[ord(s2[i])-ord('a')]-=1
            if freq2==freq1:
                return True
        return False
        
            