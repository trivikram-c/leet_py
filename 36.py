# https://leetcode.com/problems/valid-sudoku/submissions/1129040753/

# Beats 97% (self written)

# Concepts - dividend operator, modulo operator, typecasting a division to int, initializing multilevel list, list items can dynamically increase only by append or pop or push etc

#Is sudoku grid valid?

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = 9
        row = [0]*n
        col = [0]*n
        block = [[0]*int(n/3)]*3
        for r in range(n):
            row[r] = set()
            for c in range(n):
                if not col[c]:
                    col[c] = set()
                if (not r % 3) and (not c % 3):
                    block[r//3][c//3] = set()
                if board[r][c] == '.':
                    continue
                if board[r][c] in row[r]:
                    return False
                if board[r][c] in col[c]:
