class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        maxA=-math.inf
        r=len(height)-1
        while l<r:
            if height[l]<height[r]:
                area=(r-l)*height[l]
                maxA=max(area,maxA)
                l+=1
            else:
                area=(r-l)*height[r]
                maxA=max(area,maxA)
                r-=1
        return maxA