#User function Template for python3

class Solution:
    
    #Function to find the maximum number of activities that can
    #be performed by a single person.
    def activitySelection(self,n,start,end):
        

        d = []
        
        for i in range(n):
            d.append([start[i], end[i]])
        d.sort(key = lambda x:x[1])
        
        res = []
        res.append(d[0])
        
        k = 0
        for i in range(1,n):
            if d[i][0] > d[k][1]:
                res.append(d[i])
                k = i
                
        return len(res)
                
            
        d = dict(sorted(d.items(), key = lambda x:x[1]))
        
        s = list(d.keys())
        e = list(d.values())
        
        # print(s,e)
        i = 0
        c = 0
     
        # Consider rest of the activities
        for j in range(n):
     
            # If this activity has start time greater than
            # or equal to the finish time of previously
            # selected activity, then select it
            if s[j] >= e[i]:
                c+=1
                i = j
        
        # code here
        return c

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        start = list(map(int,input().strip().split()))
        end = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.activitySelection(n,start,end))
# } Driver Code Ends