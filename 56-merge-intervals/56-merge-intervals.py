class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        res=[]
        for i,interval in enumerate(intervals):
            if len(res)==0:
                res.append(interval)
            prev_end=res[-1][1]
            curr_start=interval[0]
            curr_end=interval[1]
            if prev_end>=curr_start:
                res[-1][1]=max(res[-1][1],curr_end)
            else:
                res.append(interval)
                
        return res