class Solution(object):
    def __init__(self):
        self.memo = {}

    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if not s1:
            return True if s2 == s3 else False

        if not s2:
            return True if s1 == s3 else False

        if not s3:
            return False

        l1, l2, l3 = len(s1), len(s2), len(s3)
        if self.memo.get((l1,l2,l3)) is not None:
            return self.memo[(l1,l2,l3)]

        if s1[0] == s3[0] and s2[0] == s3[0]:
            ans = (self.isInterleave(s1[1:], s2, s3[1:]) or self.isInterleave(s1, s2[1:], s3[1:]))

        elif s1[0] == s3[0]:
            ans = self.isInterleave(s1[1:], s2, s3[1:])

        elif s2[0] == s3[0]:
            ans = self.isInterleave(s1, s2[1:], s3[1:])

        else:
            ans = False

        self.memo[(l1, l2, l3)] = ans
        return ans
