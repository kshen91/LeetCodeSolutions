#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: cylisery@outlook.com

import time

def timing(f):
    def wrap(*args):
        time1 = time.time()
        ret = f(*args)
        time2 = time.time()
        print '%s function took %0.3f ms' % (f.func_name, (time2-time1)*1000.0)
        return ret
    return wrap

@timing
def isPattern(s, p):
    if len(p) == 0:
        return (len(s) == 0)

    firstMatch = len(s) != 0 and (p[0] in {s[0], '.'})

    if len(p) >= 2 and p[1] == '*':
        return (firstMatch and isPattern(s[1:], p)) or isPattern(s, p[2:])

    return (firstMatch and isPattern(s[1:], p[1:]))

@timing
def isPatternRecursiveWithMemo(s, p):
    memo = dict()

    def isPatternRecursive(i, j):
        if (i, j) in memo:
            return memo[(i, j)]

        if j == len(p):
            return i == len(s)

        firstMatch = i < len(s) and p[j] in {s[i],'.'}
        
        if j <= len(p)-2 and p[j+1] == '*':
            ans = (firstMatch and isPatternRecursive(i+1, j)) or isPatternRecursive(i, j+2)
        else:
            ans = firstMatch and isPatternRecursive(i+1, j+1)

        memo[(i, j)] = ans
        return ans

    return isPatternRecursive(0, 0)
