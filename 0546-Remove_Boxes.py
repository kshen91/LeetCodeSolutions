class Solution(object):
    def __init__(self):
        self.memo = {}

    def removeBoxes(self, boxes):
        """
        :type boxes: List[int]
        :rtype: int
        """
        n = len(boxes)
        if n < 2:
            return n

        key = tuple(boxes)
        if self.memo.get(key):
            return self.memo[key]

        if len(set(boxes)) == 1:
            ans = n*n

        else:
            ans = self.removeBoxes(boxes[1:]) + 1
            start = 0
            for i in xrange(1, n):
                if boxes[i] == boxes[0]:
                    if i - start == 1:  # neibour has same color
                        start += 1
                        ans = max(ans, (start+1)**2 + self.removeBoxes(boxes[i+1:]))
                    else:
                        ans = max(ans, self.removeBoxes(boxes[:start+1]+boxes[i:]) + self.removeBoxes(boxes[start+1:i]))

        self.memo[key] = ans
        return ans
