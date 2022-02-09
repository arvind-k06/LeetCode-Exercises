class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        lmin = prices[0]
        pmax = 0
        
        for i in range(1, len(prices)):
            if lmin>prices[i]:
                lmin = prices[i]
            
            if prices[i]-lmin>pmax:
                pmax = prices[i]-lmin
                
        
        return pmax
        