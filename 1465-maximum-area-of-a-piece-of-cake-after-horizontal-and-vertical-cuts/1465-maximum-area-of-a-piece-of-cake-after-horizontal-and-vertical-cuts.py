class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        maxVer=0
        maxHor=0
        horizontalCuts.sort()
        verticalCuts.sort()
        horizontalCuts = [0] + horizontalCuts + [h]
        verticalCuts = [0] + verticalCuts + [w]
#         if len(horizontalCuts)==1:
#             maxHor=max(h-horizontalCuts[0],horizontalCuts[0])
#         if len(verticalCuts)==1:
#             maxVer=max(w-verticalCuts[0],verticalCuts[0])
        
        for i in range(1,len(horizontalCuts)):
            hor=horizontalCuts[i]-horizontalCuts[i-1]
            maxHor=max(hor,maxHor)
        for j in range(1,len(verticalCuts)):
            ver=verticalCuts[j]-verticalCuts[j-1]
            maxVer=max(ver,maxVer)
        return (maxVer*maxHor)%((10**9)+7)        
        
        