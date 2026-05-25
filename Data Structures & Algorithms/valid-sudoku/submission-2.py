class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check First Row wise 
        # O(N2) TIME AND SPACE O(N) IF N*N SUDOKU
        # for row in range(9):
        #     seen = set()
        #     for col in range(9):
        #         val = board[row][col]
        #         if val ==".":
        #             continue
        #         if val in seen:
        #             return False
        #         seen.add(val) 
        # # check Columns wise 
        # for row in range(9):
        #     seen = set()
        #     for col in range(9):
        #         val = board[col][row]
        #         if val ==".":
        #             continue
        #         if val in seen:
        #             return False
        #         seen.add(val)    
        # # Check For boxes :
        
        # for boxrow in range(3):
        #     for boxcol in range(3):
        #         seen = set()
        #         for i in range(9):
        #             # row = (boxrow*3) + (i//3)
        #             # col = (boxcol*3) + (i%3)
        #             val = board[row][col]
        #             if val ==".":
        #                 continue
        #             if val in seen:
        #                 return False
        #             seen.add(val)
        # return True   

        cols = defaultdict(set)
        rows = defaultdict(set)
        box = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                if (board[r][c] in rows[r] or 
                    board[r][c] in cols[c] or 
                    board[r][c] in box[(r//3 ,c//3)]) :
                    return False

                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                box[(r//3 ,c//3)].add(board[r][c])

        return True              






