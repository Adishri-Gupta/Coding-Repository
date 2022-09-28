class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
#         ans=math.inf
#         for i in range(len(nums)):
#             sumV=0
#             for j in range(i,len(nums)):
#                 sumV+=nums[j]
#                 if sumV>=target:
#                     ans=min(ans,j-i+1)
#                     break
#         return ans if ans!=math.inf else 0
        curr=0
        ans=math.inf
        left,i=0,0
        while i<len(nums):
            curr+=nums[i]
            if curr>=target:
                while curr>=target:
                    
                    ans=min(ans,i-left+1)
                    
                    curr-=nums[left]
                    left+=1
            i+=1
                    
        return ans if ans!=math.inf else 0 
                
        