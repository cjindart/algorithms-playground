class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        elems = m*n

        L = 0
        R = elems - 1

        while L <= R:
            M = (L+R) // 2
            row = M // n
            col = M % n
            if matrix[row][col] < target:
                L = M + 1
            elif matrix[row][col] > target:
                R = M - 1
            else:
                return True
        return False

