class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        rows = len(image)
        cols = len(image[0])
        
        ctoc = image[sr][sc]
        
        def dfs(r,c):
            # nonlocal rows, cols, image, newColor, ctoc
            
            if r<0 or c<0 or r>rows-1 or c>cols-1 or image[r][c] == newColor or image[r][c] != ctoc:
                return
            image[r][c] = newColor
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
            
        dfs(sr,sc)
        
        return image
            
        