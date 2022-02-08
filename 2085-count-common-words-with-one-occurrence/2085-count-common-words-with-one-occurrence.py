class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        
        d1 = {}
        d2 = {}
        c = 0
        for i in words1:
            d1[i] = d1.get(i,0) + 1
        for i in words2:
            d2[i] = d2.get(i,0) + 1
            
        for i in d1:
            if d1[i] == 1 and i in d2 and d2[i] == 1:
                c+=1
                
        return c
            
        