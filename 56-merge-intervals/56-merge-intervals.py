class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        merge=[]
        for i,val in enumerate(intervals):
            if len(merge)==0 or merge[-1][1]<val[0]:
                merge.append(val)
            else:
                merge[-1][1]=max(val[1],merge[-1][1])
        return merge