class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        if len(words) == 0:
            return []

        curLength = len(words[0])
        curList = [words[0]]
        ret = []

        for word in words[1:]:
            if curLength + len(word) + len(curList) > maxWidth:
                ret.append(self.connectWords(curList, curLength, maxWidth, False))
                curLength = len(word)
                curList = [word]
            else:
                curLength += len(word)
                curList.append(word)

        ret.append(self.connectWords(curList, curLength, maxWidth, True))
        return ret

    def connectWords(self, words, curLength, maxWidth, isLastLine):
        if isLastLine:
            string = ' '.join(words)
            return string + ' '*(maxWidth - len(string))

        else:
            if len(words) == 1:
                return words[0] + ' '*(maxWidth - len(words[0]))

            needFill = maxWidth - curLength
            repeat =  needFill / (len(words)-1)
            extra = needFill % (len(words)-1)

            ret = words[0]
            for word in words[1:]:
                duplicates = repeat+1 if extra > 0 else repeat
                ret += ' '*duplicates + word
                extra -= 1

            return ret
