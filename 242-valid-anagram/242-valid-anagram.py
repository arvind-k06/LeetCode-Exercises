class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
#         if len(s)!=len(t): return False
        
#         if set(s)!=set(t): return False
        
        for i in range(len(s)):
            if s[i] in t:
                t = t.replace(s[i], "", 1)
            else:
                return False
                # print(t)
            
        # print(t)
        if t=="": return True
            
        
        return False
        