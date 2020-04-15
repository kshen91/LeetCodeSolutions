class Solution(object):
    def __init__(self):
        self.finished = False

    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        self.board = board
        self.backtrace(0)

    def getPossibleNums(self, x, y):
        ret = []

        def getGridNums(x, y):
            grid = []
            x, y = x/3*3, y/3*3
            for i in range(3):
                for j in range(3):
                    grid.append(self.board[x+i][y+j])
            return grid

        for ch in '123456789':
            if ch not in self.board[x]:
                if ch not in [row[y] for row in self.board]:
                    if ch not in getGridNums(x, y):
                        ret.append(ch)
        return ret

    def backtrace(self, count):
        if count == 81:
            self.finished = True

        if self.finished:
            return

        x, y = count/9, count % 9
        if self.board[x][y] == '.':
            nums = self.getPossibleNums(x, y)
            if len(nums) == 0:
                return

            for num in nums:
                self.board[x][y] = num
                self.backtrace(count+1)
                if self.finished:
                    return
                self.board[x][y] = '.'
        else:
            self.backtrace(count+1)
