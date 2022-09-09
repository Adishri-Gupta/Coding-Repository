class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        pointsDict={}
        maxLen=1
        for i in range(len(points)):
            [x,y]=points[i]
            for j in range(i+1, len(points)):
                [x1,y1]=points[j]
                if x1-x==0:
                    m=math.inf
                    c=x1
                else:
                    m=(y1-y)/(x1-x)
                    c=y1-m*x1
                if (m,c) in pointsDict:
                    pointsDict[(m,c)].add((x1,y1))
                    pointsDict[(m,c)].add((x,y))
                else:
                    pointsDict[(m,c)]=set([(x1,y1),(x,y)])

                
                
        for val in pointsDict.values():
            lenofSet=len(val)
            maxLen=max(lenofSet,maxLen)
        return maxLen
                