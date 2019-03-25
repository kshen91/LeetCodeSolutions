from collections import defaultdict

class Solution(object):
    def wordSquares(self, words):
        """
        :type words: List[str]
        :rtype: List[List[str]]
        """
        n = len(words[0]) # all words same length
        output = []
        prefixes = defaultdict(list)
            
        for word in words:
            for i in range(len(word)):
                prefixes[word[:i]].append(word)
            
        def helper(cur):
            if len(cur) == n:
                output.append(cur)
                return
        
            prefix = ''
            for word in cur:
                prefix += word[len(cur)]

            for word in prefixes[prefix]:
                helper(cur + [word])
                
        for i, word in enumerate(words):
            helper([word])
            
        return output
