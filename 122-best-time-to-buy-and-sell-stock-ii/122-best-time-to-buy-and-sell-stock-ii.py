class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if not prices or len(prices)==1:
            return 0
        p = 0
        for i in range(1, len(prices)):
            if prices[i]>prices[i-1]:
                p += prices[i] - prices[i-1]
            
        return p
        