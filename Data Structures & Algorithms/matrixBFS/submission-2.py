class Solution:

    found = False

    def shortestPath(self, grid: List[List[int]]) -> int:

        # get rows, cols, set, queue
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        queue = deque()
        if grid[0][0] == 1:
            return -1

        queue.append((0,0))
        visit.add((0,0))

        # loop through non empty queue (each length + 1)
        length = 0
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                # check if at end
                if r == ROWS - 1 and c == COLS - 1:
                    self.found = True
                    return length
                
                # def directions
                neigh = [[0,1], [0, -1], [1, 0], [-1, 0]]
                for dr, dc in neigh:
                    if (min(r + dr, c + dc) < 0 or r + dr == ROWS or c + dc == COLS or (r + dr, c + dc) in visit or grid[r + dr][c + dc] == 1):
                        continue
                    queue.append((r + dr, c + dc))
                    visit.add((r + dr, c + dc))
            length += 1
        
        if self.found:
            return length
        return -1


            
            