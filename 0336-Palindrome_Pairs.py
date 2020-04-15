class TrieNode(object):
    def __init__(self, value):
        self.value = value
        self.index = -1
        self.children = {}
        self.palindromeIndexes = []

class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        root = TrieNode(None)
        ans = []
        emptyIndex = -1

        for index, word in enumerate(words):
            tmp = root
            
            for i in xrange(len(word)-1, -1, -1):
                if tmp.children.get(word[i]) is None:
                    tmp.children[word[i]] = TrieNode(word[i])
                    
                if self.isPalindrome(word[:i+1]):
                    tmp.palindromeIndexes.append(index)
                
                tmp = tmp.children[word[i]]
                
            tmp.index = index
        
        for index, word in enumerate(words):
            self.search(word, index, root, ans)
            if word == '':
                emptyIndex = index
                
        if emptyIndex != -1:
            for index, word in enumerate(words):
                if index != emptyIndex and self.isPalindrome(word):
                    ans.append([index, emptyIndex])
                    
        return ans
            
    def search(self, word, index, root, ans):
        tmp = root
        for i in xrange(len(word)):
            if tmp.children.get(word[i]) is None:
                    return
            
            if tmp.children[word[i]].index != -1 and tmp.children[word[i]].index != index:
                #another word already finished
                if self.isPalindrome(word[i+1:]):
                    ans.append([index, tmp.children[word[i]].index])
                    
            tmp = tmp.children[word[i]]
                
        for i in tmp.palindromeIndexes:
            if i != index:
                ans.append([index, i])              
        
    def isPalindrome(self, word):
        i = 0
        j = len(word)-1
        
        while i < j:
            if word[i] != word[j]:
                return False
            i += 1
            j -= 1
            
        return True
