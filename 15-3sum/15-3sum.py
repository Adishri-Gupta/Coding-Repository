class Solution:
    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        x = set()
        for i in range(len(nums)):
            if nums[i] in x:
                continue
            else:
                x.add(nums[i])
            print(nums[i])
                
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
        return res
                    