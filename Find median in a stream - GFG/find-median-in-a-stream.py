#{ 
#Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys
import heapq
from collections import  defaultdict
import math


 # } Driver Code Ends
#User function Template for python3

''' 
use globals min_heap and max_heap, as per declared in driver code
use heapify modules , already imported by driver code
'''

class Solution:
    
    def __init__(self):
        self.minheap = []
        self.maxheap = []
        
    
    
    def balanceHeaps(self):
        
        if len(self.minheap) > len(self.maxheap)+1:
            heapq.heappush(self.maxheap, -1*(heapq.heappop(self.minheap)))
            
        if len(self.maxheap) > len(self.minheap):
            heapq.heappush(self.minheap, -1*(heapq.heappop(self.maxheap)))
        #Balance the two heaps size , such that difference is not more than one.
        # code here
        
        
    '''    
    You don't need to call getMedian it will be called itself by driver code
    for more info see drivers code below.
    '''
    def getMedian(self):
        
        if len(self.maxheap) == len(self.minheap):
            return (-1*self.minheap[0] + self.maxheap[0])//2
            
        elif len(self.minheap)> len(self.maxheap):
            return -1*self.minheap[0]
            
        else:
            return self.maxheap[0]
        # return the median of the data received till now.
        # code here
        
        
    def insertHeaps(self,x):
        heapq.heappush(self.minheap, -1*x)
        
        if self.minheap and self.maxheap and (-1*self.minheap[0]>self.maxheap[0]):
            heapq.heappush(self.maxheap, -1*heapq.heappop(self.minheap))
        
        self.balanceHeaps()
        #:param x: value to be inserted
        #:return: None
        # code here

#{ 
#Driver Code Starts.

if __name__ == '__main__':
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        ob=Solution()
        for i in range(n):
            x=int(input())
            ob.insertHeaps(x)
            print(math.floor(ob.getMedian()))

#} Driver Code Ends