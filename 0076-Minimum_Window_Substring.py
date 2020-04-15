from collections import Counter

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if s is None or t is None:
            return ""
        
        if len(s) < len(t):
            return ""
        
        start = 0
        end = 0
        min_start = 0
        min_len = len(s) + 1
        dict_t = Counter(t)
        search_len = len(t)
        
        for end in range(len(s)):
            if s[end] in dict_t.keys():
                dict_t[s[end]] -= 1
                if dict_t[s[end]] >= 0:
                    search_len -= 1
                
            while search_len == 0:
                if end - start + 1 < min_len:
                    min_len = end - start + 1
                    min_start = start

                if s[start] in dict_t.keys():
                    dict_t[s[start]] += 1
                    if dict_t[s[start]] > 0:
                        search_len += 1

                start += 1
                
        return "" if len(s) < min_len else s[min_start: min_start + min_len] 
