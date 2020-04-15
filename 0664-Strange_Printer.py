class Solution(object):
    def strangePrinter(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        memo = {}

        def helper(i, j):
            if i == j:
                return 1
            if i > j:
                return 0
            if memo.get((i, j)):
                return memo[(i, j)]

            # assume last element is not same as any previous one
            ans = helper(i, j-1) + 1
            for k in xrange(i, j): # k = i ~ j-1
                if s[k] == s[j]:
                    ans = min(ans, helper(i, k-1) + helper(k+1, j))

            memo[(i, j)] = ans
            return ans

        return helper(0, len(s)-1)
