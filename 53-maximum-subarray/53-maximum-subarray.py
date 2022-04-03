class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        global_sum = nums[0]
        local_sum = 0
        for i in nums:
            local_sum+=i
            global_sum = max(local_sum, global_sum)
            if local_sum<0:
                local_sum = 0            
            
            
        return global_sum
                
        