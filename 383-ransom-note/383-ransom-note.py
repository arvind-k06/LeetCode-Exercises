class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r = ransomNote
        m = magazine
        
        for i in range(len(r)):
            if r[i] in m:
                b = m.index(r[i])
                m = m[0:b]+m[b+1:]
            
            else:
                return False
            
        return True
        