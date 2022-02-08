class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        
        if nums.count(0) == 0:
            return
        i = nums.index(0)
        j = i+1
        if i == -1 or len(nums) == 1 or i == len(nums)-1:
            return

        while(i<len(nums) and j<len(nums)):
            
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i+=1
            j+=1