class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        prefixSum=[0]*(len(nums)+1)
        mapPre={}
        ans=0
        prefixSum[1]=nums[0]
        for i in range(1,len(nums)):
            prefixSum[i+1]=prefixSum[i]+nums[i]
        
        for i, pre in enumerate(prefixSum):
            diff=pre-k
            if diff in mapPre:
                cur_ans = i - mapPre[diff]
                ans = max(ans, cur_ans)
            
            if pre not in mapPre:
                mapPre[pre]=i
        print(mapPre)
        return ans