class Trie(object):
    def __init__(self):
        self.root = {}

    def insert(self, word):
        p = self.root
        for c in word:
            if c not in p:
                p[c] = {}
            p = p[c]
        p['#'] = True
    
    def searchByPrefix(self, prefix, results):
        node = self._find(prefix)
        if node is None:
            return None
        
        for key in node.keys():
            if key == '#':
                results.append(prefix)
            else:
                self.searchByPrefix(prefix+key, results)
        
        return results
    
    def _find(self, prefix):
        p = self.root
        for c in prefix:
            if c not in p:
                return None
            p = p[c]
        return p

class Solution(object):
    def wordSquares(self, words):
        """
        :type words: List[str]
        :rtype: List[List[str]]
        """
        if words is None or len(words) == 0:
            return words
        
        self.trie = Trie()
        for word in words:
            self.trie.insert(word)
            
        self.ret = []
        self.targetLen = len(words[0])
        
        for word in words:
            self.search([word])
                
        return self.ret

    def search(self, result):
        currentLen = len(result)
        if currentLen == self.targetLen:
            from copy import deepcopy
            self.ret.append(deepcopy(result))
        else:
            prefix = ''
            for word in result:
                prefix += word[currentLen]
        
            validStrs = self.trie.searchByPrefix(prefix,[])
            if validStrs is not None:
                for word in validStrs:
                    result.append(word)
                    self.search(result)    # execute for all strings in order to find all possibilities
                    result.pop()
