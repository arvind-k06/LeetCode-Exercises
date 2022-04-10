#User function Template for python3

'''
class Pair(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b
'''

def maxChainLen(Parr, n):
    
    
    p = Parr
    d = []
    for i in p:
        d.append([i.a, i.b])
        
    d.sort(key = lambda x:x[1])
    # print(d)
    
    c = 1
    k = 0
    for i in range(1,n):
        # print(i,k)
        if d[k][1] < d[i][0]:
            k=i
            c+=1
            
    return c
    # Parr:  list of pair
    #code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

class Pair(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b

if __name__ =='__main__':
    tcs = int(input())

    for _ in range(tcs):
        n=int(input())

        arr=[int(x) for x in input().split()]

        Parr=[]

        i=0
        while n*2>i:

            Parr.append(Pair(arr[i],arr[i+1]))

            i+=2

        #print(Parr,len(Parr))

        print(maxChainLen(Parr, n))
# } Driver Code Ends