from collections import Counter
from copy import copy

class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        strLen = len(s)
        nrOfWords = len(words)

        if strLen == 0 or nrOfWords == 0:
            return []

        wordLen = len(words[0])
        k = wordLen * nrOfWords
        if k > strLen:
            return []

        ret = []
        wordsCnt = Counter(words)

        for i in xrange(strLen-k+1):
            if self.CanConcatenate(s[i:i+k], wordLen, wordsCnt):
                ret.append(i)

        return ret

    def CanConcatenate(self, s, wordLen, wordsDict):
        d = copy(wordsDict)
        for i in xrange(0, len(s), wordLen):
            substr = s[i:i+wordLen]
            cnt = d.get(substr)
            if cnt is None:
                return False

            if cnt == 0:
                return False

            d[substr] -= 1

        return True
