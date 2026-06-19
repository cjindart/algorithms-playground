class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        start_color = image[sr][sc]
        

        def dfs(image, r, c, color, start_color, visit):
            ROWS, COLS = len(image), len(image[0])
            
            # out of bounds
            if (min(r, c) < 0 or r == ROWS or c == COLS or (r, c) in visit or image[r][c] != start_color):
                return 
            # found valid square to color
            image[r][c] = color
            
            
            visit.add((r, c))

            dfs(image, r+1, c, color, start_color, visit)
            dfs(image, r-1, c, color, start_color, visit)
            dfs(image, r, c+1, color, start_color, visit)
            dfs(image, r, c-1, color, start_color, visit)

        dfs(image, sr, sc, color, start_color, set())
        return image