class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet=set(nums)
        longCon=0
        maxLen=0
        
        for num in numSet:
            if num-1 not in numSet:
                longCon=1
                currNum=num
                
                while currNum+1 in numSet:
                    longCon+=1
                    currNum+=1
            maxLen=max(longCon,maxLen)
        return maxLen