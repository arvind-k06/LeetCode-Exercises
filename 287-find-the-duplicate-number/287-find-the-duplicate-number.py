class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        s = f = fin = 0
        
        while True:
            s = nums[s]
            f = nums[nums[f]]
            
            if s == f:
                while fin != s:
                    s = nums[s]
                    fin = nums[fin]
                    
                return fin
        