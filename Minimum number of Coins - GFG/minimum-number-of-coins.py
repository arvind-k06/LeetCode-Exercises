#User function Template for python3

class Solution:
    def minPartition(self, N):
        # code here
        
        res = []
        
        p = [1,2,5,10,20,50,100,200,500,2000]
        
        p = p[::-1]
        
        j = 0
        if N in p:
            return [N]
        for i in range(len(p)):
            if p[i] < N:
                j=i
                break
        while(N and j>-1):
            # print(p[j] ,N)
            if N-p[j] == 0:
                res.append(p[j])
                break
            elif N-p[j]>0:
                N -= p[j]
                res.append(p[j])
            else:
                j+=1
        return res
                
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        
        ob = Solution()
        arr = ob.minPartition(N)
        for i in range(len(arr)):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends