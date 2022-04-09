#User function Template for python3

class Solution:
    def findLargest(self, N, S):
        # code here
        # if S == 0:
        #     return -1
        res = ''
        
        if S == 0:
            if N == 1:
                return 0
            else:
                return -1
        
        if S > 9*N:
            return -1
        
        for i in range(N):
            if S>=9:
                res+='9'
                S-=9
            else:
                res+=str(S)
                S = 0
                
        return int(res)
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N, S = [int(x) for x in input().split()]
        
        ob = Solution()
        print(ob.findLargest(N, S))
# } Driver Code Ends