class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        def searchFromRightToLeft(s):
            open = 0
            close = 0
            res = 0
            for i in xrange(len(s)-1,-1,-1):
                if s[i] == ')':
                    close += 1
                else:
                    open += 1
                    if close == open:
                        res = max(res, 2 * close)
                    if open > close:
                        open = 0
                        close = 0
            return res

        def searchFromLeftToRight(s):
            open = 0
            close = 0
            res = 0
            for i in xrange(len(s)):
                if s[i] == '(':
                    open += 1
                else:
                    close += 1
                    if open == close:
                        res = max(res, 2 * open)
                    if close > open:
                        close = 0
                        open = 0

            return res

        return max(searchFromLeftToRight(s), searchFromRightToLeft(s))
