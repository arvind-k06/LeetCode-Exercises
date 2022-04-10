#User function Template for python3

class Solution:
    def minOperation(self, n):
        # code here 
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