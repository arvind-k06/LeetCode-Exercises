from collections import Counter
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        
        ss = Counter(s)
        tt = Counter(t)
        
        ss1 = ss - tt
        tt1 = tt - ss
        
        return sum(ss1.values())+sum(tt1.values())
        # for i in t:
        #     if i in s:
        #         s  = s.replace(i, '', 1)
        #         t = t.replace(i,'',1)
        # return len(s)+len(t)
            
        