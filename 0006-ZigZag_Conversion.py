class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows < 2:
            return s

        groupNum = 2*numRows - 2
        numCols, rest = (len(s) / groupNum) * (numRows - 1), len(s) % groupNum
        extra = rest % numRows + 1 if rest > numRows else 1
        numCols += extra
        arr = [["" for i in range(numCols)] for j in range(numRows)]
        
        x = y = 0
        normal = True
        for ch in s:
            arr[y][x] = ch

            if normal:
                y += 1
                if y == numRows-1:
                    normal = False
            else:
                y -= 1
                x += 1
                if y == 0:
                    normal = True
                    
        res = ''
        for row in arr:
            res += ''.join(row)
            
        return res
