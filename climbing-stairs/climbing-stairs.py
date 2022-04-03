class Solution:
    def climbStairs(self, n: int) -> int:
        l = []
        l.append(1)
        l.append(2)
        
        if n == 1 : return l[0]
        if n == 2: return l[1]
        
        for i in range(3,n+1):
            l.append(l[-1]+l[-2])
            
        return l[-1]