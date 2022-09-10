class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        res=0
        n=len(costs)
        red=costs[0][0]
        blue=costs[0][1]
        green=costs[0][2]
        prered=red
        preblue=blue
        pregreen=green
        for i in range(1, n):
            red=min(preblue,pregreen)+costs[i][0]
            blue=min(prered,pregreen)+costs[i][1]
            green=min(prered,preblue)+costs[i][2]
            preblue=blue
            prered=red
            pregreen=green
        return min(red,blue,green)