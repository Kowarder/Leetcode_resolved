# 36. Valid Sudoku
# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:
#A Sudoku board (partially filled) could be valid but is not necessarily solvable.
#Only the filled cells need to be validated according to the mentioned rules.
#Input: board = 
#[["5","3",".",".","7",".",".",".","."]
#,["6",".",".","1","9","5",".",".","."]
#,[".","9","8",".",".",".",".","6","."]
#,["8",".",".",".","6",".",".",".","3"]
#,["4",".",".","8",".","3",".",".","1"]
#,["7",".",".",".","2",".",".",".","6"]
#,[".","6",".",".",".",".","2","8","."]
#,[".",".",".","4","1","9",".",".","5"]
#,[".",".",".",".","8",".",".","7","9"]]
#Output: true
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        sub_boxes = collections.defaultdict(set)

        for row in range(9):
            for col in range(9):
                num = board[row][col]
                if num == '.':
                    continue
                if (num in rows[row] or 
                    num in cols[col] or
                    num in sub_boxes[(row//3, col//3)]
                ):
                    return False

                rows[row].add(num)
                cols[col].add(num)
                sub_boxes[(row//3, col//3)].add(num)

        return True
# using collections.defaultdict(set) to create three list which include the number of each row, column and 3x3 subbox. using set looks like ["1": {1,2}]
# iterate each number of the original list, skip '.', record the number to the list
# if the number already restored in the one of three lists, it means this row, column or sub-box has the same number which means false
# if not, add this number to this row, column and subbox
