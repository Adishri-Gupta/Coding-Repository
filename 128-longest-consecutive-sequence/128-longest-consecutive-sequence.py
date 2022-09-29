class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet=set(nums)
        currStreak=0
        longStreak=0
        for num in numSet:
            
            if num-1 not in numSet:
                currStreak=1
                curr=num
                
                while curr+1 in numSet:
                    currStreak+=1
                    curr+=1
                
                
                longStreak=max(longStreak,currStreak)
                
                
        return longStreak
                
        