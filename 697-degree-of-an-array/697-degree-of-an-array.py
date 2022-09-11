class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        mapVal = defaultdict(list)
        minLen=math.inf
        for i, n in enumerate(nums):
            if n in mapVal: 
                mapVal[n].append(i)
            else: 
                mapVal[n] = [i]
        M = max([len(i) for i in mapVal.values()])
        
        for i in mapVal.values():
            if len(i)==M:
                minLen=min(minLen,i[-1]-i[0]+1)
        return minLen
                
            