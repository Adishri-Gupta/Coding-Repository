class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        res=0
        n=len(costs)
        red=costs[0][0]
        blue=costs[0][1]
        green=costs[0][2]
        for i in range(1, n):
            red,blue,green=min(blue,green)+costs[i][0],min(red,green)+costs[i][1],min(red,blue)+costs[i][2]
        return min(red,blue,green)