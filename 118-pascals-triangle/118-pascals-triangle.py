class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        n = numRows
        if n == 1: return [[1]]
        if n == 2: return [[1], [1,1]]
        
        arr = [[1], [1,1]]
        
        for i in range(2, n):
            l = [1]
            # t = arr[i-1]
            for j in range(len(arr[i-1])-1):
                l.append(arr[i-1][j]+arr[i-1][j+1])
            l.append(1)
            arr.append(l)
            
        return arr