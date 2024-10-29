class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(9):
            col = [board[j][i] for j in range(9)]
            row = [board[i][j] for j in range(9)]
            if not self.isValid(row) or not self.isValid(col):
                return False
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                box = [board[x][y] for x in range(i, i+3) for y in range(j, j+3)]
                if not self.isValid(box):
                    return False
        return True
    
    def isValid(self, target):
        elements = [x for x in target if x != '.']
        return len(elements) == len(set(elements))
