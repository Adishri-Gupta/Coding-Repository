class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minBuy=math.inf
        maxPro=0
        for i in range(len(prices)):
            if prices[i]<minBuy:
                minBuy=prices[i]
            elif prices[i]-minBuy>maxPro:
                maxPro=prices[i]-minBuy
        return maxPro
                