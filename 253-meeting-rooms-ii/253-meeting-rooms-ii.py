class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        meetingEnd = []
        heapq.heapify(meetingEnd)
        maxRooms=1
        intervals.sort(key =  lambda x:x[0])
        heapq.heappush(meetingEnd, intervals[0][1])
        for i in range(1,len(intervals)):
        
            if meetingEnd[0]>intervals[i][0]:
                heapq.heappush(meetingEnd,intervals[i][1])
          
            else:
                while meetingEnd and meetingEnd[0]<=intervals[i][0]:
                    heapq.heappop(meetingEnd)
                heapq.heappush(meetingEnd,intervals[i][1])
            maxRooms = max(maxRooms, len(meetingEnd))
                
        return maxRooms
            
    
        
    
    
    