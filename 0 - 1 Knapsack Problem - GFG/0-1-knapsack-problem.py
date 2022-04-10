#User function Template for python3

class Solution:
    
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val, n):
        # print(W, wt, val, n)
        
        
        
        dp = [[0]*(W+1) for _ in range(n+1)]
        
        for i in range(n+1):
            for w in range(W+1):
                if i == 0 or w == 0:
                    dp[i][w] = 0
                    
                elif wt[i-1] <= w:
                    dp[i][w] = max(val[i-1]+dp[i-1][w-wt[i-1]], dp[i-1][w])
                    
                else:
                    dp[i][w] = dp[i-1][w]
                    
        return dp[n][W]
        
        # if n == 0 or W == 0:
        #     return 0
            
        # if wt[n-1] > W:
        #     return self.knapSack(W,wt,val,n-1)
            
        # else:
        #     return max((val[n-1] + self.knapSack(W-wt[n-1], wt, val, n-1)), (self.knapSack(W, wt, val, n-1)))
       
        # # code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        W = int(input())
        val = list(map(int,input().strip().split()))
        wt = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.knapSack(W,wt,val,n))
# } Driver Code Ends