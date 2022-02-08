class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        arr = []
        n = len(nums)
        r = (n-k)%n
        if n == 1:
            return 1
        while(r<n):
            arr.append(nums[r])
            r+=1
        
        for i in range((n-k)%n):
            arr.append(nums[i])
            
        nums[:] = arr
        """
        Do not return anything, modify nums in-place instead.
        """
        