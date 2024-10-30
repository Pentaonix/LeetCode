from collections import defaultdict
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        row = defaultdict(set)
        col = defaultdict(set)
        cell = defaultdict(set)
        for i in range(9):
            for j in range(9):
                if (((board[i][j] in row[i])
                    or (board[i][j] in col[j])
                    or (board[i][j] in cell[i//3,j//3]))
                    and board[i][j] != '.'):
                        return False
                else:
                    row[i].add(board[i][j])
                    col[j].add(board[i][j])
                    cell[i//3,j//3].add(board[i][j])
        return True
