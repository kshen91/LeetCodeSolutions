class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        ls, lt = len(s), len(t)
        if ls < lt:
            return 0

        if lt == 0:
            return 1

        dp = [[0] * ls for _ in xrange(lt)]

        for t_i in xrange(lt):
            for s_i in xrange(t_i, ls):
                if t[t_i] == s[s_i]:
                    if s_i > 0 and t_i > 0:
                        dp[t_i][s_i] = dp[t_i-1][s_i-1] + dp[t_i][s_i-1]
                    elif t_i == 0 and s_i > 0:
                        dp[t_i][s_i] = dp[t_i][s_i-1] + 1
                    else:
                        dp[t_i][s_i] = 1
                else:
                    dp[t_i][s_i] = dp[t_i][s_i-1] if s_i > 0 else 0

        return dp[-1][-1]
