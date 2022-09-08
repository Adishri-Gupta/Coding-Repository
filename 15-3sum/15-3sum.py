class Solution:
    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        
        i = 0
        while i<len(nums):                
            if nums[i]>0:
                break
                
            j=i+1
            k=len(nums)-1
            while j<k:
                sumVal=nums[j]+nums[k]+nums[i]
                if sumVal<0:
                    j+=1
                    while j<k and j+1<len(nums) and nums[j-1] == nums[j]:
                        j+=1
                elif sumVal>0:
                    k-=1
                    while j<k and k>-1 and nums[k+1] == nums[k]:
                        k-=1
                else:
                    res.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1
                    while j<k and j+1<len(nums) and nums[j-1] == nums[j]:
                        j+=1
            i+=1
            while i<len(nums) and nums[i-1] == nums[i]:
                i+=1
        return res
                    