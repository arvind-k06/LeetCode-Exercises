class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        globalmax = float('-inf')
        
        localsum =0
        
        for i in nums:
            localsum+=i
            
            if localsum>globalmax:
                globalmax = localsum
            
            if localsum<0:
                localsum=0
                
        return globalmax
        