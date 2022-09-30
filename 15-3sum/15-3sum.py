class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=set()
        for i in range(len(nums)):
            j=i+1
            k=len(nums)-1
            while j<k:
                sumVal=nums[j]+nums[k]+nums[i]
                if sumVal<0:
                    j+=1
                elif sumVal>0:
                    k-=1
                else:
                    res.add((nums[i],nums[j],nums[k]))
                    j+=1
                    k-=1
        return list(res)
                    
     