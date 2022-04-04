class Solution:
    def maxArea(self, height: List[int]) -> int:
        h = height
        l = 0
        r = len(h)-1
        a = 0
        while(l<r):
            a = max(a, (r-l)*(min(h[l], h[r])))
            
            if h[l]<h[r]: l+=1
            else: r-=1
                
        return a
        