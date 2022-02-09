class Solution:
    def reverseString(self, s: List[str]) -> None:
        
        def reverse(i, j, s):
            if i>=j:
                return
            else:
                s[i], s[j] =  s[j], s[i]
                reverse(i+1, j-1, s)
        
        reverse(0, len(s)-1, s)
        
#         i = 0
#         j = len(s)-1
        
#         while(i<=j):
#             s[i], s[j] = s[j], s[i]
#             i+=1
#             j-=1
        """
        Do not return anything, modify s in-place instead.
        """
        