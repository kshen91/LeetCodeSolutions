class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        # construct a histogram and calculate it's max area for each line, whose time complexity is O(n)
        if len(matrix) == 0:
            return 0

        ret = 0
        histogram = [0] * len(matrix[0])

        for line in matrix:
            for i in xrange(len(histogram)):
                histogram[i] = histogram[i] + 1 if line[i] == '1' else 0

            ret = max(ret, self.maxAreaOfHistogram(histogram))

        return ret

    def maxAreaOfHistogram(self, array):
        stack = []  # store (value, index)
        maxArea = 0

        for i, h in enumerate(array):
            while stack and stack[-1][0] > h:
                val, index = stack.pop()
                if stack:
                    maxArea = max((i-stack[-1][1]-1)*val, maxArea)
                else:
                    maxArea = max(i*val, maxArea)

            stack.append((h, i))

        # calculate the rest values left in stack
        while stack:
            val, index = stack.pop()
            if stack:
                maxArea = max(maxArea, (len(array)-stack[-1][1]-1)*val)
            else:
                maxArea = max(maxArea, len(array)*val)

        return maxArea
