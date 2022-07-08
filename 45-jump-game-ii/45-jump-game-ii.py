class Solution:
    def jump(self, nums: List[int]) -> int:
        max_Reach=0
        jumps=0
        curr_Reach=0
        for i in range(len(nums)-1):
            max_Reach=max(max_Reach,i+nums[i])
                
            if i==curr_Reach:
                jumps+=1
                curr_Reach=max_Reach
                
        return jumps