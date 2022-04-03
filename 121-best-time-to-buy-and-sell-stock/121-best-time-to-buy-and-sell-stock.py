class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        lmin = prices[0]
        pmax = 0
        
        for i in prices:
            if i<lmin: lmin = i
            if i-lmin > pmax: pmax = i-lmin
                
        return pmax
        