class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip()
        
        if len(s) == 0:
            return False

        if 'L' in s:
            return False

        if ' ' in s:
            return False
        
        if '++' in s or '+-' in s or '-+' in s or '--' in s:
            return False

        if s[0] == '+' or s[0] == '-':
            s = s[1:]

        try:
            eval(s)
        except:
            if s.isdigit():
                return True
            return False

        plusPos = s.find('+')
        minusPos = s.find('-')
        if ( plusPos != -1 and plusPos != 0 and s[plusPos-1] != 'e') or (minusPos != -1 and minusPos != 0 and s[minusPos-1] != 'e'):
            return False

        return True
