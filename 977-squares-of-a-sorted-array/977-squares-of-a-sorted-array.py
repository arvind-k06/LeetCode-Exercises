class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        arr = []
        
        i=0
        j = len(nums)-1
        
        while(i<=j):
            if abs(nums[i]) < abs(nums[j]):
                arr.append(nums[j]**2)
                j-=1
            else:
                arr.append(nums[i]**2)
                i+=1
        
        return arr[::-1]