#User function Template for python3

class Solution:
    def numberOfPaths (self, n, m):
        dp = [[0 for i in range(m)] for j in range(n)]
        
        for i in range(m):
            dp[0][i] = 1
            
        for j in range(n):
            dp[j][0] = 1
            
        for i in range(1,n):
            for j in range(1,m):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        # print(dp)
        return dp[n-1][m-1]


#{ 
#  Driver Code Starts
#Initial Template for Python 3

        

if __name__ == '__main__': 
    ob = Solution()
    t = int (input ())
    for _ in range (t):
        m, n = map(int, input().split())
        ans = ob.numberOfPaths(m, n)
        print(ans)




# } Driver Code Ends