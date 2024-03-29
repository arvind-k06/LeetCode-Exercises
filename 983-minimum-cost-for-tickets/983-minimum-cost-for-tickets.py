class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        dp = [0]*366
        
        for i in range(1,366):
            if i not in days:
                dp[i] = dp[i-1]
            else:
                dp[i] = min(costs[0]+dp[i-1], costs[1]+dp[max(0, i-7)], costs[2]+dp[max(0, i-30)])
                
        return dp[365]
        