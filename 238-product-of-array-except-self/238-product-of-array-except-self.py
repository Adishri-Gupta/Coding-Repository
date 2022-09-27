class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        R,L,ans=[0]*n,[0]*n,[0]*n
        L[0],R[n-1] = 1,1
        for i in range(1, n):
            L[i]=L[i-1]*nums[i-1]
        for j in reversed(range(n-1)):
            R[j]=R[j+1]*nums[j+1]
        
        for i in range(n):
            ans[i]=L[i]*R[i]
        return ans
            
        