class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        r = rowIndex
        
        if r == 0 : return [1]
        if r == 1 : return [1,1]
        
        ans, prev = [], [1,1]
        
        for i in range(2,r+1):
            ans = [1]
            for j in range(len(prev)-1):
                ans.append(prev[j]+prev[j+1])
            ans.append(1)
            
            prev = ans
            
        return ans
                
            
        
        
        