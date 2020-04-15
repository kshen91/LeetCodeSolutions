class Solution(object):
    def numWays(self, steps, arrLen):
        """
        :type steps: int
        :type arrLen: int
        :rtype: int
        """
        # with step n, in order to be able to return to origin point, max distance can travel is n/2 + 1
        if arrLen == 1:
            return 1

        arrLen = min(arrLen, steps/2 + 1)

        # dp[i][j] stands for the numWays of step i to location j
        # dp[i][j] = dp[i-1][j-1] + dp[i-1][j] + dp[i-1][j+1]
        dp = [[0 for _ in xrange(arrLen)] for _ in xrange(steps+1)]
        dp[0][0] = 1

        for i in xrange(1, steps+1):
            for j in xrange(arrLen):
                if j == 0:
                    dp[i][j] = dp[i-1][0] + dp[i-1][1]
                elif j == arrLen-1:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j] + dp[i-1][j+1]

        return dp[steps][0] % (10**9+7)
