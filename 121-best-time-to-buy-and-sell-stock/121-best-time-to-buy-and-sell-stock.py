class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        lmin = prices[0]
        pmax = 0
        
        for i in prices:
            lmin = min(i, lmin)
            pmax = max(pmax, i-lmin)
            
            print(pmax)
        return pmax
        