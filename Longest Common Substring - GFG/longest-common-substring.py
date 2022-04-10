#User function Template for python3

class Solution:
    def longestCommonSubstr(self, X, Y, m, n):
        
        LCSuff = [[0 for k in range(n+1)] for l in range(m+1)]

        # To store the length of
        # longest common substring
        result = 0
        
        # Following steps to build
        # LCSuff[m+1][n+1] in bottom up fashion
        for i in range(m + 1):
            for j in range(n + 1):
                if (i == 0 or j == 0):
                    LCSuff[i][j] = 0
                elif (X[i-1] == Y[j-1]):
                    LCSuff[i][j] = LCSuff[i-1][j-1] + 1
                    result = max(result, LCSuff[i][j])
                else:
                    LCSuff[i][j] = 0
        return result
        
        X = S1
        Y= S2
        m = len(S1)
        n = len(S2)
        
        # declaring the array for storing the dp values
        L = [[None]*(n + 1) for i in range(m + 1)]
        
        """Following steps build L[m + 1][n + 1] in bottom up fashion
        Note: L[i][j] contains length of LCS of X[0..i-1]
        and Y[0..j-1]"""
        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0 or j == 0 :
                    L[i][j] = 0
                elif X[i-1] == Y[j-1]:
                    L[i][j] = L[i-1][j-1]+1
                else:
                    L[i][j] = max(L[i-1][j], L[i][j-1])
        print(L)
        
        # L[m][n] contains the length of LCS of X[0..n-1] & Y[0..m-1]
        return L[m][n]
        dp = [[0]*(m+1) for _ in range(n+1)]
        
        for i in range(0,n+1):
            for j in range(0,m+1):
                # print(i,j)
                if i == 0 or j==0:
                    dp[i][j] = 0
                if S1[i-1] == S2[j-1]:
                    dp[i][j] = 1+dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
                    
        return dp[n][m]
        # code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        n,m = input().strip().split(" ")
        n,m = int(n), int(m)
        S1 = input().strip()
        S2 = input().strip()
        
        
        ob=Solution()
        print(ob.longestCommonSubstr(S1, S2, n, m))
# } Driver Code Ends