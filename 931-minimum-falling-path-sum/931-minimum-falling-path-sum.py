class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n=len(matrix)
     
        
        for i in range(1,n):
            for j in range(0,n):
                if j==0:
                    matrix[i][j]=matrix[i][j]+min(matrix[i-1][j+1],matrix[i-1][j])
                elif j==n-1:
                    matrix[i][j]=matrix[i][j]+min(matrix[i-1][j],matrix[i-1][j-1])
                else:
                    matrix[i][j]=matrix[i][j]+min(matrix[i-1][j+1],matrix[i-1][j-1],matrix[i-1][j])
        return min(matrix[n-1])