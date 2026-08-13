class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board[0])

        rowD = defaultdict(set)
        colD = defaultdict(set)
        squD = defaultdict(set)

        for r in range(n):
            for c in range(n):
                # at certain square board[r][c]
                item = board[r][c]
                if item == ".":
                    continue

                if (item in rowD[r] or item in colD[c] or item in squD[(r // 3, c // 3)]):
                    return False
                    
                rowD[r].add(item)
                colD[c].add(item)
                squD[(r // 3, c // 3)].add(item)
        return True