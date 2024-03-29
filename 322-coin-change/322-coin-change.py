class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        
        dp = [[0]*(amount+1) for _ in range(len(coins)+1)]
        
        for i in range(1, amount+1):
            dp[0][i] = float('inf')
            
        for i in range(1, len(coins)+1):
            for j in range(1, amount+1):
                
                if j < coins[i-1]:
                    dp[i][j] = dp[i-1][j]
                    
                else:
                    t = 1+dp[i][j-coins[i-1]]
                    l = dp[i-1][j]
                    dp[i][j] = min(t,l)
        # print(dp)
        if dp[-1][-1] == float('inf'): return -1
        return dp[-1][-1]