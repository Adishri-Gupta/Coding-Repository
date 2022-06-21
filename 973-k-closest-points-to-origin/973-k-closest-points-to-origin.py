class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        closestPoints = []
        finalPoints = []
        
        for point in points:
            distance = math.sqrt(math.pow(point[0],2)+math.pow(point[1],2))
            closestPoints.append([distance, point[0],point[1]])
        heapq.heapify(closestPoints)
        for i in range(k):
            dist,x,y = heapq.heappop(closestPoints)
            finalPoints.append([x,y])
        return finalPoints
        