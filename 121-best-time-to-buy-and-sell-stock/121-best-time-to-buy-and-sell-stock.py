class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        minprice=float('inf')
        for i in range(len(prices)):
            res=max(res, prices[i]-minprice)
            minprice=min(minprice, prices[i])
                    
        return res