class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        
        # max_k = 2
        n = len(prices)
        ## dp[i][k][0] represents the max profit for day i with k times transactions with not holding a stock
        # dp = [[[0, 0] for _ in xrange(max_k+1)] for _ in xrange(n)]
        
#         for i in xrange(n):
#             dp[i][0][0] = 0
#             dp[i][0][1] = -float('inf')
        
        # for i in xrange(n):
        #     for k in xrange(max_k,0,-1):
        #         if i == 0:
        #             dp[0][k][0] = 0
        #             dp[0][k][1] = -prices[0]
        #         else:
        #             dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
        #             dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])
        
        # return dp[n-1][max_k][0]
        dpi10, dpi20, dpi11, dpi21 = 0, 0, -prices[0], -prices[0]
        
        for i in xrange(n):
            dpi20 = max(dpi20, dpi21 + prices[i])
            dpi21 = max(dpi21, dpi10 - prices[i])
            dpi10 = max(dpi10, dpi11 + prices[i])
            dpi11 = max(dpi11, -prices[i])
            
        return dpi20
