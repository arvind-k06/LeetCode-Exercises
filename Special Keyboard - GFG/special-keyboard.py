#User function Template for python3

class Solution:
    def optimalKeys(self, N):
        
        if N<=6:
            return N
            
        d = [0]*(N)
        
        for i in range(1, 7):
            d[i-1] = i
            
        for n in range(7,N+1):
            
            for b in range(n-3, 0, -1):
                c = (n-b-1)*d[b-1]
                d[n-1] = max(c, d[n-1])
                
        return d[N-1]
            
        
        # code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        
        ob = Solution()
        print(ob.optimalKeys(N))
# } Driver Code Ends