class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        total = sum(nums)
        n = len(nums)
        l = 0
        curr = 0
        ctr=0
        maxOper=-1

        for r in range(n):
            curr += nums[r]
            while curr > total-x and l <= r:
                curr -= nums[l]
                l+= 1
            if curr == total-x:
                maxOper=max(maxOper,r-l+1)
        if maxOper!=-1:
            return n-maxOper
        else: 
            return -1
        