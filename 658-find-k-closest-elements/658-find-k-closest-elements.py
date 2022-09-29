class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        res=[]
        n=len(arr)
     
        minHeap=[]
        
        for i in range(n):

            diff=abs(arr[i]-x)
            heapq.heappush(minHeap, [-diff,-i])
            if len(minHeap)>k:
                heapq.heappop(minHeap)
        for i in range(k):
            index= -minHeap[i][1]
            res.append(arr[index])
        res.sort()
        return res
            
        