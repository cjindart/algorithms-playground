class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid[0])
        m = len(obstacleGrid)
        
        prevRow = [0] * n

        for r in range(m - 1, -1, -1):
            curRow = [0] * n
            if obstacleGrid[r][n-1] != 1:
                if r == m - 1:
                    curRow[n - 1] = 1
                else:
                    curRow[n - 1] = prevRow[n - 1]
            else:
                curRow[n - 1] = 0

            for c in range(n - 2, -1, -1):
                if obstacleGrid[r][c] == 1:
                    curRow[c] = 0
                else:
                    curRow[c] = prevRow[c] + curRow[c+1]

            prevRow = curRow
        
        return prevRow[0]