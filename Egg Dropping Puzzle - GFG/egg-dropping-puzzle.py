#User function Template for python3

class Solution:
    
    #Function to find minimum number of attempts needed in 
    #order to find the critical floor.
    def eggDrop(self,K, N):
        M = 300 # big enough number
        dp = [[0 for j in range(K+1)] for i in range(M+1)]
        # Initialization 1 --> no move no floor --> dp[0][*] = 0
        # Initialization 2 --> no egg no floor --> dp[*][0] = 0
        # General case --> we want to find dp[m][k] --> we pick one egg and drop (1 move)
        #              --> now we have k or k-1 eggs, depending on whether the previous egg is broken
        #              --> so in either case, we can at least sum up 1 (first move) + dp[m-1][k] + dp[m-1][k-1] 
        for i in range(1, M+1):
            for j in range(1, K+1):
                dp[i][j] = 1 + dp[i-1][j] + dp[i-1][j-1]
                if dp[i][j] >= N:
                    return i
                
            
        
        # for i in range(n):
        #     for j in range(k):
                
        #         if i == 0 or j == 0:
        #             dp[i][j] = 0
        #         elif i == 1:
        #             d[i][j] = j
        #         elif j == 1:
        #             dp[i][j] = i
        #         else:
        #             m = -1
        #             for x in range(k):
        #                 m = max()

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
        n,k = map(int,input().strip().split())
        ob=Solution()
        print(ob.eggDrop(n,k))
# } Driver Code Ends