class Solution:
    max_isl = 0

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        

        def dfs(grid, r, c, visit):
            ROWS, COLS = len(grid), len(grid[0])

            if (min(r, c) < 0 or r == ROWS or c == COLS or (r, c) in visit or grid[r][c] != 1):
                return 0 
            
            grid[r][c] = 2
            visit.add((r, c))
            count = 1
            
            count += dfs(grid, r+1, c, visit)
            count += dfs(grid, r-1, c, visit)
            count += dfs(grid, r, c+1, visit)
            count += dfs(grid, r, c-1, visit)

            return count


        visit = set()
        ROWS, COLS = len(grid), len(grid[0])
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    
                    count = dfs(grid, r, c, visit)
                    if count > self.max_isl:
                        self.max_isl = count
        print(grid)
        return self.max_isl
                    




