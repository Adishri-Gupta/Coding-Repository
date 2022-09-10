class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        k=len(costs[0])
        n=len(costs)
        mat = [costs[0][i] for i in range(k)]
        for i in range(1,n):
            
            for j in range(k):
                costs[i][j]=min(costs[i-1][0:j]+costs[i-1][j+1:])+costs[i][j]
                mat[j]=costs[i][j]
        return min(mat)