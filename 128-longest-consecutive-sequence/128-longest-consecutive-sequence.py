class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mapLong=set(nums)
        maxlen = 0
        
        for i in nums:
            if i-1 not in mapLong:
                
                current = i
                length = 1
                
                while current + 1 in mapLong:
                    current = current + 1
                    length += 1
                    
                maxlen = max(maxlen, length)
        return maxlen
                
        
        
        
        
        
        
        
        
        
        lcs=0
        visited=set()
        
        if len(nums)==1:
            return 1
      
        for i in range(len(nums)):
            if nums[i]+1 in mapLong and nums[i]+1 not in visited:
                lcs+=1
                visited.add(nums[i]+1)
            elif nums[i]-1 in mapLong and nums[i]-1 not in visited:
                lcs+=1
                visited.add(nums[i]-1)
        return lcs
    
    
                
                
            