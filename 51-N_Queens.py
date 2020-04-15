class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        
        base = [['.'] * n for i in range(n)]
        ret = []
        
        def checkObliqueCells(row, col):
            # only smaller rows need to be checked
            colMinus = col - 1
            colPlus = col + 1
            row = row - 1
            
            while row >= 0:
                if colMinus >= 0 and base[row][colMinus] == 'Q':
                    return False
                if colPlus < n and base[row][colPlus] == 'Q':
                    return False
                
                row -= 1
                colMinus -= 1
                colPlus += 1
                
            return True
            
        def getPossibleColumns(row):
            cols = []
            for col in range(n):
                if 'Q' not in [base[i][col] for i in range(row)] and checkObliqueCells(row, col):
                    cols.append(col)
                    
            return cols
        
        def traceback(row):
            if row == n:
                solution = [''.join(base[i]) for i in range(n)]
                ret.append(solution)
                return
            
            possibleCols = getPossibleColumns(row)
            if len(possibleCols) == 0:
                return
            
            for col in possibleCols:
                base[row][col] = 'Q'
                traceback(row + 1)
                base[row][col] = '.'
                
        traceback(0)

        return ret
