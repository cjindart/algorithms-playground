class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefix = []
        for row in matrix:
            r = []
            total = 0
            for num in row:
                total += num
                r.append(total)
            self.prefix.append(r)
        # print(self.prefix)


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = 0
        for row in range(row1, row2+1):
            if col1 > 0:
                leftsum = self.prefix[row][col1 - 1]
            else:
                leftsum = 0
            rightsum = self.prefix[row][col2]
            total += (rightsum - leftsum)
        
        return total


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)