class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        # paint all adj 1s with 2
        def dfs(grid, r, c, visit):
            ROWS, COLS = len(grid), len(grid[0])
            if (min(r, c) < 0 or r == ROWS or c == COLS or (r, c) in visit or grid[r][c] != "1"):
                return
            grid[r][c] = "2"
            visit.add((r, c))

            dfs(grid, r+1, c, visit)
            dfs(grid, r-1, c, visit)
            dfs(grid, r, c+1, visit)
            dfs(grid, r, c-1, visit)



        count = 0
        # loop through rows and cols, if 1 found, add to count and run DFS to grab all adjacent
        ROWS, COLS = len(grid), len(grid[0])

        visit = set()

        for r in range(ROWS):
            for c in range(COLS):
                # print(grid[r][c])
                if grid[r][c] == "1":
                    # print("yes")
                    dfs(grid, r, c, visit)
                    count += 1
        # print(grid)
        return count 