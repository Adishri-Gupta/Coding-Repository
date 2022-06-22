class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        minHeap=[]
        
        for i in range(len(heights)-1):
            jump=heights[i+1]-heights[i]
            if jump>0:
                heapq.heappush(minHeap,heights[i+1]-heights[i])
                
            if jump<=0:
                continue
            if len(minHeap)>ladders:
                bricksUsed=heapq.heappop(minHeap)
                bricks-=bricksUsed
            
            if bricks<0:
                return i
        return len(heights)-1