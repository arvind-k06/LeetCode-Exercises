#User function Template for python3

class Solution:
    def minOperation(self, n):
        # code here
        dp = [0]*(n+1)
        if n<4:
            return n
        dp[1] = 1
        dp[2] = 2
        dp[3] = 3
        
        for i in range(4, n+1):
            if i%2 == 1:
                dp[i] = 1+dp[i-1]
                
            else:
                dp[i] = 1+dp[i//2]
                
        return dp[n]
        
        res = 0
        if n<2:
            return n
            
        else:
            
            if n%2 == 1:
                res = 1 + self.minOperation(n-1)
            else:
                res = 1 + self.minOperation(n//2)
                
        return res

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        ob = Solution()
        print(ob.minOperation(n))
# } Driver Code Ends