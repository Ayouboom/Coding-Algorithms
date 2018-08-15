"""
Author : Ayoub Omari
Date: 15/08/2018

Problem : Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.
"""

def isMatch(self, s, p):
    memo = [[False for _ in range(len(p)+1)] for _ in range(len(s)+1)]

    memo[0][0] = True # p and s empty

    # first line
    for j in range(1, len(p)+1):
        if p[j-1] == '*':
            if j > 1:
                memo[0][j] = memo[0][j-2]
            else:
                memo[0][j] = True

    #The first column is all False except the 0th line : empty pattern and non empty string

    for i in range(1, len(s)+1):
        for j in range(1, len(p)+1):
            if s[i-1]==p[j-1] or p[j-1]=='.':
                memo[i][j] = memo[i-1][j-1] #delete them and compare sub pattern and sub string

            elif p[j-1]=='*':
                if j > 1:
                    if p[j-2]==s[i-1] or p[j-2]=='.':
                        memo[i][j] = memo[i-1][j] # more than one time
                    memo[i][j] = memo[i][j] or memo[i][j-1] or memo[i][j-2] #many OR one OR 0 times

    return memo[-1][-1]
