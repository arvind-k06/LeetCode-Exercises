class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        
        c = nums.count(0)
        v = c
        while(c):
            nums.remove(0)
            c-=1

        while(v):
            nums.append(0)
            v-=1
        """
        Do not return anything, modify nums in-place instead.
        """
        