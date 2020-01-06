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
        if firstMatch:
            return isPattern(s[1:], p)
        return isPattern(s, p[2:])

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
            if firstMatch:
                ans = isPatternRecursive(i+1, j)
            else:
                ans = isPatternRecursive(i, j+2)
        else:
            ans = firstMatch and isPatternRecursive(i+1, j+1)

        memo[(i, j)] = ans
        return ans

    return isPatternRecursive(0, 0)

@timing
def isPatternDP(s, p):
    i = len(s) - 1
    j = len(p) - 1

    while (i > 0 and j > 0):
        if p[j] in {s[i], '.'}:
            i -= 1
            j -= 1
        elif p[j] == '*' and j >= 1:
            if p[j-1] == s[i]:
                i -= 1
            else:
                j -= 2
        else:
            return False

    return (i==0)
