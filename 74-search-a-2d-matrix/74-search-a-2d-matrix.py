class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, h = 0, len(matrix)-1
        while l<=h:
            mid = l + (h-l)//2
            row = matrix[mid]
            if target<row[0]: h = mid-1
            elif target>row[-1]: l = mid+1
            else: 
                lo, hi = 0, len(row)-1
                while(lo<=hi):
                    mid=lo+(hi-lo)//2
                    if target==row[mid]:
                        return True
                    elif target>row[mid]:
                        lo=mid+1
                    else:
                        hi=mid-1
                return False
        return False