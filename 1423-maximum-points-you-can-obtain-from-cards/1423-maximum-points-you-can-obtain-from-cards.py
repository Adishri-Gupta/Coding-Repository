class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        total=sum(cardPoints)
    
        l=0
        r=len(cardPoints)-k
        maxP=sum(cardPoints[r:])
        total=maxP
        while r<=len(cardPoints)-1:
            maxP +=cardPoints[l]-cardPoints[r]
            total=max(total,maxP)
            l+=1
            r+=1
        return total
            
            