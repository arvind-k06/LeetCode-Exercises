class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        n = len(mat) * len(mat[0])
        n1 = r*c
        
        if n!=n1:
            return mat
        
        arr = []
        for i in mat:
            arr.extend(i)
        arr = arr[::-1]
#         print(arr)
        
        
#         for i in range(len(mat)):
#             for j in range(len(mat[i])):
#                 print(i,j, mat[i][j])
                
        a = []
        for i in range(r):
            t = []
            for j in range(c):
                t.append(arr.pop())
            
            a.append(t)
        return a