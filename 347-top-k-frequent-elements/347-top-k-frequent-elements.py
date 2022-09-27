class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt=Counter(nums)
        minHeap=[]
        ans=[]
        print(cnt)
        heapq.heapify(minHeap)
        
        for c in cnt.keys():
            heapq.heappush(minHeap,[cnt[c],c])
            if len(minHeap)>k:
                heapq.heappop(minHeap)
        print(minHeap)
        for i in range(k):
            ans.append(minHeap[i][1])
        return ans            
            