class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longCon= 0
        valSet=set(nums)
        
        for num in valSet:
            if num-1 not in valSet:
                
                currVal=num
                lenVal=1
                
                while currVal+1 in valSet:
                    lenVal+=1
                    currVal+=1
                longCon = max(longCon,lenVal)
        return longCon