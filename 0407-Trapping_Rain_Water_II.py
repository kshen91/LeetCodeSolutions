from heapq import heappush, heappop

class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        m = len(heightMap)
        n = len(heightMap[0]) if m != 0 else 0
        
        if not all([m, n]):
            return 0

        ans = 0
        
        # enqueue the boarder into priority queue and update visited array
        q = []
        visited = [[False] * n for _ in xrange(m)]
        
        for i in xrange(m):
            if i == 0 or i == m-1:
                r = xrange(n)
            else:
                r = [0, n-1]

            for j in r:
                heappush(q, (heightMap[i][j], i*n+j))
                visited[i][j] = True                                
                    
        # pop from queue and visit neighbors
        waterlevel = 0

        while q:
            cell = heappop(q)
            waterlevel = max(waterlevel, cell[0])
            x, y = cell[1]/n, cell[1]%n
            if visited[x][y] != True:
                visited[x][y] = True
                if waterlevel > cell[0]:
                    ans += (waterlevel - cell[0])

            neighborCoors = self.getNotVisitedNeighborCoors(x, y, m, n, visited)
            for [i, j] in neighborCoors:
                heappush(q, (heightMap[i][j], i*n+j))
                    
        return ans
    
    def getNotVisitedNeighborCoors(self, x, y, m, n, visited):
        coors = []
        if x-1 >= 0 and not visited[x-1][y]:
            coors.append([x-1, y])
        if x+1 < m and not visited[x+1][y]:
            coors.append([x+1, y])
        if y-1 >= 0 and not visited[x][y-1]:
            coors.append([x, y-1])
        if y+1 < n and not visited[x][y+1]:
            coors.append([x, y+1])
                
        return coors
     
