# User function Template for python3

class Solution:
    # Complete this function
    
    #Function to find equilibrium point in the array.
    def equilibriumPoint(self,A, N):
        
        tsum = sum(A)
        lsum = 0
        for i in range(N):
            lsum+=A[i]
            if lsum == tsum:
                return i+1
            else:
                tsum-=A[i]
        return -1
        # if N==1:
        #     return 1
            
        # pre_sum = 0
        
        # pre = [0]
        
        # for i in range(1,N):
        #     pre_sum+=A[i-1]
        #     pre.append(pre_sum)
            
        # pos_sum = 0
        # post = [0]*N
        # for i in range(N-2,-1,-1):
        #     pos_sum+=A[i+1]
        #     post[i] = pos_sum
            
        # for i in range(N):
        #     if pre[i] == post[i]:
        #         return i+1
        # return -1
            
            
        # print(pre, post)
        # for i in range(N):
        #     if sum(A[:i]) == sum(A[i+1:]):
        #         return i+1
                
        return -1
        # Your code here


#{ 
#  Driver Code Starts
# Initial Template for Python 3

import math


def main():

    T = int(input())

    while(T > 0):

        N = int(input())

        A = [int(x) for x in input().strip().split()]
        ob=Solution()

        print(ob.equilibriumPoint(A, N))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends