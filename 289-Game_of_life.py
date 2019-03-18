# Rules:
# 1. Any live cell with fewer than two live neighbours dies, as if by underpopulation.
# 2. Any live cell with two or three live neighbours lives on to the next generation.
# 3. Any live cell with more than three live neighbours dies, as if by overpopulation.
# 4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
# Input:
# [
#   [0,1,0],
#   [0,0,1],
#   [1,1,1],
#   [0,0,0]
# ]
# Output:
# [
#   [0,0,0],
#   [1,0,1],
#   [0,1,1],
#   [0,1,0]
# ]

class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if board is None or len(board) == 0:
            return

        rowNr = len(board)
        colNr = len(board[0])

        for i in range(rowNr):
            for j in range(colNr):
                lives = self.GetLives(board, i, j, rowNr, colNr)

                # assume there's 2 bits to indicate (next state, current state)
                # then by default 'next state' is always 0
                # we can get next state later by doing board[i][j] >> 1
                if board[i][j] == 1 and (lives == 2 or lives == 3): # rule 2
                    board[i][j] = 3 # 3 -> 0b11
                if board[i][j] == 0 and lives == 3: #rule 4
                    board[i][j] = 2 # 2 -> 0b10

        # update state
        for i in range(rowNr):
            for j in range(colNr):
                board[i][j] >>= 1

    def GetLives(self, board, i, j, rowNr, colNr):
        lives = 0

        for x in range(max(0,i-1), min(rowNr, i+2)):
            for y in range(max(0,j-1), min(colNr, j+2)):
                lives += board[x][y] & 1      # 0bxx & 0b01 = 0b0x, which is current state

        lives -= board[i][j] & 1
        return lives
