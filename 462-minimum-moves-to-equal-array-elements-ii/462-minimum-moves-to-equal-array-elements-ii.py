class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        m = int(median(nums))
        
        moves = 0
        
        for i in range(len(nums)):
            moves+=abs(nums[i]-m)
            
        return moves