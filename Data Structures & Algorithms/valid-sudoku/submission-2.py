class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # create three sets (cols, rows, squ)

        cols = defaultdict(set)
        rows = defaultdict(set)
        sqa = defaultdict(set)

        n = len(board[0])

        for r in range(n):
            for c in range(n):
                item = board[r][c]
                if item == ".":
                    continue
                
                if item in cols[c] or item in rows[r] or item in sqa[(r // 3, c // 3)]:
                    return False
                
                cols[c].add(item)
                rows[r].add(item)
                sqa[(r // 3, c // 3)].add(item)
        
        return True 