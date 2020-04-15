class Solution(object):
    def __init__(self):
        self.memo = {}

    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if self.memo.get((s1,s2)) is not None:
            return self.memo[(s1,s2)]

        n = len(s1)
        if n == 0:
            return True

        if n == 1:
            self.memo[(s1,s2)] = (s1 == s2)
            return s1 == s2

        if n == 2:
            self.memo[(s1,s2)] = (s1 == s2 or s1 == (s2[1]+s2[0]))
            return self.memo[(s1,s2)]

        for i in range(1, n):
            ans = self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]) or \
                self.isScramble(s1[:i], s2[n-i:]) and self.isScramble(s1[i:], s2[:n-i])
            if ans:
                self.memo[(s1,s2)] = True
                return True

        self.memo[(s1,s2)] = False
        return False
