class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        [start, end] = newInterval
        l, r = [], []
        for interval in intervals:
            if interval[1] < start:
                l.append(interval)
            elif interval[0] > end:
                r.append(interval)
            else:
                start = min(start, interval[0])
                end = max(end, interval[1])

        return l + [[start, end]] + r
