#User function Template for python3
import bisect
class Solution:
    
    #Function to find length of longest increasing subsequence.
    def longestSubsequence(self,a,n):
        
        f = []
        
        for i in range(len(a)):
            if not f or f[-1]<a[i]:
                f.append(a[i])
            else:
                p = bisect.bisect_left(f, a[i])
                f[p] = a[i]
                
        return len(f)
        
        
        dp = [[0]*(n+1) for _ in range(n+1)]
        m = 0
        a = [0]+a
        for i in range(1, n+1):
            for j in range(1, n+1):
                if a[i-1]>a[j-1]:
                    dp[i][j] = 1+dp[i-1][j-1]
                    m = max(m, dp[i][j])
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        # print(dp)
        return dp[-1][-1]
        # code here
       


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        a = [ int(x) for x in input().split() ]
        ob=Solution()
        print(ob.longestSubsequence(a,n))
# } Driver Code Ends