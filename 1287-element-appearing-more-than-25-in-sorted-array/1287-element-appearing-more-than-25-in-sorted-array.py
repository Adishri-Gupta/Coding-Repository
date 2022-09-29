class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n=len(arr)
        candidates=[n//4,n//2,3*n//4]
        

        def firstocc(nums,target):
            l=0
            r=len(nums)-1
            ans=-1
            while l<=r:
                mid=(l+r)//2
                if nums[mid]==target:
                    ans=mid
                    r=mid-1
                elif nums[mid]<target:
                    l=mid+1
                else:
                    r=mid-1
            return ans
        def lastocc(nums,target):
            l=0
            r=len(nums)-1
            ans=-1
            while l<=r:
                mid=(l+r)//2
                if nums[mid]==target:
                    ans=mid
                    l=mid+1
                elif nums[mid]<target:
                    l=mid+1
                else:
                    r=mid-1
            return ans
        for c in candidates:
            first=firstocc(arr,arr[c])
            last=lastocc(arr,arr[c])
            if last-first+1>n/4:
                return arr[c]
    
    