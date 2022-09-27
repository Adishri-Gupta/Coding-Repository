class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        maxEnd=max([v[1] for v in intervals])
        
        arr=[0]*(maxEnd+2)
        arrSum=0
        for start,end in intervals:
            arr[start]+=1
            arr[end]-=1
            
        for i in range(1, len(arr)):
            arr[i]+=arr[i-1]
        return max(arr)
            
    
        
    
    
    