class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:


        def dfs(grid, r, c, visit):
            ROWS, COLS = len(grid), len(grid[0])

            # bounds checking, checking if 1, or already visited
            if (min(r, c) < 0 or r == ROWS or c == COLS or (r, c) in visit or grid[r][c] == 1):
                return 0
            
            # if we are at the end, return 1 valid way
            if r == ROWS - 1 and c == COLS - 1:
                return 1
            
            visit.add((r, c))

            count = 0
            count += dfs(grid, r + 1, c, visit)
            count += dfs(grid, r - 1, c, visit)
            count += dfs(grid, r, c + 1, visit)
            count += dfs(grid, r, c - 1, visit)

            visit.remove((r, c))
            return count


        paths = dfs(grid, 0, 0, set())
        return paths