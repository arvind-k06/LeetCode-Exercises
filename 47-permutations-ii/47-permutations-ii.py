class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        
        def dfs(nums, path, res):
            if not nums:
                res.append(path)
            else:
                for i in range(len(nums)):
                    if i>0 and nums[i] == nums[i-1]:
                        continue
                    dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)
        
        
        dfs(nums, [], res)
        return res
    
        
        