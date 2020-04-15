class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        x = y = 0
        ret = []

        # set start up config
        dir = 'right'
        
        # depends on the shape of matrix, it might end up with [] or [[],[],[]...]
        while matrix != [] and all(column != [] for column in matrix): 
            xmax = len(matrix[0]) - 1
            ymax = len(matrix) - 1

            ret.append(matrix[y][x])

            # define move direction
            if dir == 'left' and x == 0:
                dir = 'up'
                matrix = matrix[:-1]

            elif dir == 'up' and y == 0:
                dir = 'right'
                for row in matrix: del row[0]
                continue   # x already get increased by remove one column, so skip moving

            elif dir == 'right' and x == xmax:
                dir = 'down'
                matrix = matrix[1:]
                continue  # y already get increased by remove one row, so skip moving

            elif dir == 'down' and y == ymax:
                dir = 'left'
                for row in matrix: del row[-1];

            # move based on direction
            if dir == 'left':  x -= 1;
            if dir == 'right': x += 1;
            if dir == 'up':    y -= 1;
            if dir == 'down':  y += 1;

        return ret
