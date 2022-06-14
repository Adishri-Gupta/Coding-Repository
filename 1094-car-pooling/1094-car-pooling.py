class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda t:t[1])
        
        minHeap = []
        currPass = 0
        for trip in trips:
            
            numPass, start, end = trip
            while minHeap and minHeap[0][0]<=start:
                currPass-=minHeap[0][1]
                heapq.heappop(minHeap)
                
            currPass+=numPass
            if currPass>capacity:
                return False
            heapq.heappush(minHeap, [end,numPass])
        return True
        
        