class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # remove duplicated "*" in pattern
        patternInList = list(p)
        i = 0
        pre = ''
        while i < len(patternInList):
            if patternInList[i] == '*' and pre == '*':
                del patternInList[i]
            else:
                pre = patternInList[i]
                i += 1
        p = ''.join(patternInList)

        resultDict = {}

        # do matching
        def isMatchLite(s, p):
            if resultDict.get((s,p)) is not None:
                return resultDict[(s,p)]

            if len(s) == 0:
                if len(p) == 0 or p == '*':
                    return True
                return False

            if len(p) == 0:
                return False

            if p[0] not in {s[0], '?'}:
                if p[0] == '*':
                    result = isMatchLite(s, p[1:]) or isMatchLite(s[1:], p)
                else:
                    result = False

                resultDict[(s,p)] = result
                return result

            return isMatchLite(s[1:], p[1:])

        return isMatchLite(s, p)
