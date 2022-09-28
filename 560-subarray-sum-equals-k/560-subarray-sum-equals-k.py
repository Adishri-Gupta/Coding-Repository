class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum={0:1}
        res=0
        currSum=0
        for i in nums:
            currSum+=i
            diff=currSum-k
            if diff in prefixSum:
                res+=prefixSum[diff]
            if currSum in prefixSum:
                
                prefixSum[currSum]+=1
            else:
                prefixSum[currSum]=1
        return res