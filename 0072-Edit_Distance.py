class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        memo = {}

        def dp(i, j):
            if memo.get((i,j)):
                return memo[(i,j)]

            if i == -1:
                return j+1

            if j == -1:
                return i+1

            if word1[i] == word2[j]:
                memo[(i,j)] = dp(i-1, j-1)
            else:
                # (i-1, j) -> remove one from word1
                # (i, j-1) -> add one to word2
                # (i-1, j-1) -> replace 1 in word1 to word2
                memo[(i,j)] = min(dp(i-1, j)+1, dp(i, j-1)+1, dp(i-1,j-1)+1)

            return memo[(i,j)]

        return dp(len(word1)-1, len(word2)-1)
