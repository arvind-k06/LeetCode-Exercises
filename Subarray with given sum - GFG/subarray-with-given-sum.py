#User function Template for python3

#Function to find a continuous sub-array which adds up to a given number.
class Solution:
    def subArraySum(self,arr, n, s): 
        
        Sum =arr[0]
        first =0
        last=0
        while first < n and last<n:
            if Sum == s:
                return first+1,last+1
            elif Sum < s and last <n-1:
                last +=1
                Sum +=arr[last]
            else:
                Sum -= arr[first]
                first +=1
        return [-1]
    #     i = 1
    #     j =0 
        
    #     summ = arr[0]
        
    #     while(i<n):
            
    #         if summ == s:
    #             return [j+1, i]
                
    #         elif summ<s:
    #             summ+=arr[i]
    #             i+=1
                
    #         elif summ>s and j<i-1:
    #             summ-=arr[j]
    #             j+=1
                
            
            
    #         # if s == arr[i]:
    #         #     return [i+1, i+1]

    #     return [-1]
        # for a in arr:
        #     ret.append(a)
        #     while sum(ret) > s:
        #         ret.pop(0)
                
        #     if sum(ret) == s:
        #         return [arr.index(ret[0])+1, arr.index(ret[-1])+1]
        
        # return [-1]
                #Write your code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math

def main():
        T=int(input())
        while(T>0):
            
            NS=input().strip().split()
            N=int(NS[0])
            S=int(NS[1])
            
            A=list(map(int,input().split()))
            ob=Solution()
            ans=ob.subArraySum(A, N, S)
            
            for i in ans:
                print(i, end=" ")
                
            print()
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends