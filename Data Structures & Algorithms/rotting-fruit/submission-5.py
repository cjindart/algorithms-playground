class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        rotten = set()
        fresh = []


        # find rotten fruits
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r, c))
                    rotten.add((r, c))
                if grid[r][c] == 1:
                    fresh.append((r, c))
                
        if not rotten and not fresh:
            return 0
        if not rotten and fresh:
            return -1
                
        minutes = 0
        while queue:
            if not fresh:
                return minutes
            for _ in range(len(queue)):
                r, c = queue.popleft()
                
                neigh = [[0, 1], [1, 0], [0, -1], [-1, 0]]
                for dr, dc in neigh:
                    if (min(r+dr, c+dc) < 0 or r+dr == ROWS or c+dc == COLS or (r+dr, c+dc) in rotten or grid[r+dr][c+dc] != 1):
                        continue
                    queue.append((r+dr, c+dc))
                    rotten.add((r+dr, c+dc))
                    fresh.remove((r+dr, c+dc))
            minutes += 1
        
        return -1
