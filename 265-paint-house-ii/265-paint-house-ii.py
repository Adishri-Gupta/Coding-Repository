class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        k=len(costs[0])
        n=len(costs)
        mat = [costs[0][i] for i in range(k)]
        for i in range(1,n):
            newmat=mat.copy()
            for j in range(k):
                newmat[j] = min(mat[0:j] + mat[j+1:]) + costs[i][j]
            mat=newmat
        return min(mat)