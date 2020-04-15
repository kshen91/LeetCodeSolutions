from heapq import heappush, heappop

class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        points = []
        for building in buildings:
            points.extend([[building[0], -building[2]], [building[1], building[2]]])

        points.sort()
        heightq = []
        popIfMet = []

        ans = []
        for point in points:
            if point[1] < 0:
                curHeight = heightq[0] if len(heightq) > 0 else 0
                heappush(heightq, point[1])
                if point[1] < curHeight:
                    ans.append([point[0], abs(point[1])])
            else:
                if point[1] < abs(heightq[0]):
                    popIfMet.append(-point[1])

                if point[1] == abs(heightq[0]):
                    heappop(heightq)
                    while len(heightq) > 0 and heightq[0] in popIfMet:
                        popIfMet.remove(heightq[0])
                        heappop(heightq)

                    curHeight = abs(heightq[0]) if len(heightq) > 0 else 0
                    if point[1] != curHeight:
                        ans.append([point[0], curHeight])

        return ans
